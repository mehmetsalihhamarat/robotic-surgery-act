# Copyright (c) 2024, The ORBIT-Surgical Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause


import gymnasium as gym

from . import agents, ik_abs_env_cfg, ik_rel_env_cfg, joint_pos_env_cfg

##
# Register Gym environments.
##

##
# Joint Position Control
##

gym.register(
    id="Isaac-Lift-Needle-PSM-v0",
    entry_point="omni.isaac.lab.envs:ManagerBasedRLEnv",
    kwargs={
        "env_cfg_entry_point": joint_pos_env_cfg.NeedleLiftEnvCfg,
        "rsl_rl_cfg_entry_point": agents.rsl_rl_cfg.LiftNeedlePPORunnerCfg,
    },
    disable_env_checker=True,
)

gym.register(
    id="Isaac-Lift-Needle-PSM-Play-v0",
    entry_point="omni.isaac.lab.envs:ManagerBasedRLEnv",
    kwargs={
        "env_cfg_entry_point": joint_pos_env_cfg.NeedleLiftEnvCfg_PLAY,
        "rsl_rl_cfg_entry_point": agents.rsl_rl_cfg.LiftNeedlePPORunnerCfg,
    },
    disable_env_checker=True,
)

##
# Inverse Kinematics - Absolute Pose Control
##

gym.register(
    id="Isaac-Lift-Needle-PSM-IK-Abs-v0",
    entry_point="omni.isaac.lab.envs:ManagerBasedRLEnv",
    kwargs={
        "env_cfg_entry_point": ik_abs_env_cfg.NeedleLiftEnvCfg,
        "rsl_rl_cfg_entry_point": agents.rsl_rl_cfg.LiftNeedlePPORunnerCfg,
    },
    disable_env_checker=True,
)

gym.register(
    id="Isaac-Lift-Needle-PSM-IK-Abs-Play-v0",
    entry_point="omni.isaac.lab.envs:ManagerBasedRLEnv",
    kwargs={
        "env_cfg_entry_point": ik_abs_env_cfg.NeedleLiftEnvCfg_PLAY,
        "rsl_rl_cfg_entry_point": agents.rsl_rl_cfg.LiftNeedlePPORunnerCfg,
    },
    disable_env_checker=True,
)

##
# Inverse Kinematics - Relative Pose Control
##

gym.register(
    id="Isaac-Lift-Needle-PSM-IK-Rel-v0",
    entry_point="omni.isaac.lab.envs:ManagerBasedRLEnv",
    kwargs={
        "env_cfg_entry_point": ik_rel_env_cfg.NeedleLiftEnvCfg,
        "rsl_rl_cfg_entry_point": agents.rsl_rl_cfg.LiftNeedlePPORunnerCfg,
        "robomimic_bc_cfg_entry_point": "/home/nural/orbit-surgical/source/extensions/orbit.surgical.tasks/orbit/surgical/tasks/surgical/lift/config/needle/agents/robomimic/bc.json",
        "robomimic_bcq_cfg_entry_point": "/home/nural/orbit-surgical/source/extensions/orbit.surgical.tasks/orbit/surgical/tasks/surgical/lift/config/needle/agents/robomimic/bcq.json",
        "robomimic_cql_cfg_entry_point": "/home/nural/orbit-surgical/source/extensions/orbit.surgical.tasks/orbit/surgical/tasks/surgical/lift/config/needle/agents/robomimic/cql.json",
        "robomimic_iris_cfg_entry_point": "/home/nural/orbit-surgical/source/extensions/orbit.surgical.tasks/orbit/surgical/tasks/surgical/lift/config/needle/agents/robomimic/iris.json",
        "robomimic_iql_cfg_entry_point": "/home/nural/orbit-surgical/source/extensions/orbit.surgical.tasks/orbit/surgical/tasks/surgical/lift/config/needle/agents/robomimic/iql.json",
        "robomimic_gl_cfg_entry_point": "/home/nural/orbit-surgical/source/extensions/orbit.surgical.tasks/orbit/surgical/tasks/surgical/lift/config/needle/agents/robomimic/gl.json",
        "robomimic_hbc_cfg_entry_point": "/home/nural/orbit-surgical/source/extensions/orbit.surgical.tasks/orbit/surgical/tasks/surgical/lift/config/needle/agents/robomimic/hbc.json",
        "robomimic_td3_bc_cfg_entry_point": "/home/nural/orbit-surgical/source/extensions/orbit.surgical.tasks/orbit/surgical/tasks/surgical/lift/config/needle/agents/robomimic/td3_bc.json",
    },
    disable_env_checker=True,
)

gym.register(
    id="Isaac-Lift-Needle-PSM-IK-Rel-Play-v0",
    entry_point="omni.isaac.lab.envs:ManagerBasedRLEnv",
    kwargs={
        "env_cfg_entry_point": ik_rel_env_cfg.NeedleLiftEnvCfg_PLAY,
        "rsl_rl_cfg_entry_point": agents.rsl_rl_cfg.LiftNeedlePPORunnerCfg,
        "robomimic_bc_cfg_entry_point": "/home/nural/orbit-surgical/source/extensions/orbit.surgical.tasks/orbit/surgical/tasks/surgical/lift/config/needle/agents/robomimic/bc.json",
        "robomimic_bcq_cfg_entry_point": "/home/nural/orbit-surgical/source/extensions/orbit.surgical.tasks/orbit/surgical/tasks/surgical/lift/config/needle/agents/robomimic/bcq.json",
        "robomimic_cql_cfg_entry_point": "/home/nural/orbit-surgical/source/extensions/orbit.surgical.tasks/orbit/surgical/tasks/surgical/lift/config/needle/agents/robomimic/cql.json",
        "robomimic_iris_cfg_entry_point": "/home/nural/orbit-surgical/source/extensions/orbit.surgical.tasks/orbit/surgical/tasks/surgical/lift/config/needle/agents/robomimic/iris.json",
        "robomimic_iql_cfg_entry_point": "/home/nural/orbit-surgical/source/extensions/orbit.surgical.tasks/orbit/surgical/tasks/surgical/lift/config/needle/agents/robomimic/iql.json",
        "robomimic_gl_cfg_entry_point": "/home/nural/orbit-surgical/source/extensions/orbit.surgical.tasks/orbit/surgical/tasks/surgical/lift/config/needle/agents/robomimic/gl.json",
        "robomimic_hbc_cfg_entry_point": "/home/nural/orbit-surgical/source/extensions/orbit.surgical.tasks/orbit/surgical/tasks/surgical/lift/config/needle/agents/robomimic/hbc.json",
        "robomimic_td3_bc_cfg_entry_point": "/home/nural/orbit-surgical/source/extensions/orbit.surgical.tasks/orbit/surgical/tasks/surgical/lift/config/needle/agents/robomimic/td3_bc.json",
    },
    disable_env_checker=True,
)



