from env.arm import ArmEnv
from env.human import HopEnv, GaitEnv
from env.helpers import gymify_env

env = gymify_env(HopEnv(visualize=True))
env.reset()

for i in range(10000):
    env.step([i] * 24)
