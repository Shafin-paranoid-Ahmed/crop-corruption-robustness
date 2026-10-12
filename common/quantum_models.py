"""Frozen E3 inference definitions; see provenance/MODEL_SOURCES.json."""
import math
import torch
import torch.nn as nn

FUSED_DIM = 1344
HIDDEN = 128
NUM_CLASSES = 25
ANGLE_SCALE = 3.141592653589793

class FusionProjectionK(nn.Module):
    def __init__(self, bottleneck, fused_dim=FUSED_DIM, hidden=HIDDEN, dropout=0.1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(fused_dim, hidden),
            nn.BatchNorm1d(hidden),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden, bottleneck),
        )

    def forward(self, x):
        return self.net(x)

class E3VQCK(nn.Module):
    def __init__(self, bottleneck, vqc_layers, num_classes=NUM_CLASSES, sim="lightning.qubit"):
        super().__init__()
        self.bottleneck = bottleneck
        self.vqc_layers = vqc_layers
        self.projection = FusionProjectionK(bottleneck)
        from common.quantum_layer import VQCLayer
        self.vqc = VQCLayer(n_qubits=bottleneck, n_layers=vqc_layers, sim=sim)
        self.readout = nn.Linear(bottleneck, num_classes)

    def forward(self, x):
        z = ANGLE_SCALE * torch.tanh(self.projection(x))
        z = self.vqc(z)
        return self.readout(z)

    def post_bottleneck_parameters(self):
        return self.vqc.parameters()

def alpha_parameter_init(alpha_init, alpha_bounded, alpha_max):
    if not alpha_bounded:
        return float(alpha_init)
    if alpha_max <= 0:
        raise ValueError("--alpha-max must be positive when --alpha-bounded is enabled")
    ratio = max(min(float(alpha_init) / float(alpha_max), 0.999), -0.999)
    return math.atanh(ratio)

def effective_alpha(alpha_param, alpha_bounded, alpha_max):
    if alpha_bounded:
        return float(alpha_max) * torch.tanh(alpha_param)
    return alpha_param

class E3VQCKResidual(nn.Module):
    def __init__(
        self,
        bottleneck,
        vqc_layers,
        num_classes=NUM_CLASSES,
        sim="lightning.qubit",
        alpha_init=0.1,
        alpha_bounded=False,
        alpha_max=1.0,
    ):
        super().__init__()
        base = E3VQCK(bottleneck, vqc_layers, num_classes=num_classes, sim=sim)
        self.bottleneck = bottleneck
        self.vqc_layers = vqc_layers
        self.projection = base.projection
        self.vqc = base.vqc
        self.readout = base.readout
        self.alpha_bounded = bool(alpha_bounded)
        self.alpha_max = float(alpha_max)
        init = alpha_parameter_init(alpha_init, self.alpha_bounded, self.alpha_max)
        self.alpha = nn.Parameter(torch.tensor(init, dtype=torch.float32))

    def effective_alpha(self):
        return effective_alpha(self.alpha, self.alpha_bounded, self.alpha_max)

    def forward(self, x):
        z = torch.tanh(self.projection(x))
        q = self.vqc(ANGLE_SCALE * z)
        z = z + self.effective_alpha() * q
        return self.readout(z)

    def post_bottleneck_parameters(self):
        yield from self.vqc.parameters()
        yield self.alpha
