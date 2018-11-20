import magent


def get_config(map_size):
    gw = magent.gridworld
    cfg = gw.Config()
    cfg.set({"minimap_mode": True})
    cfg.set({"map_width": map_size, "map_height": map_size})
    attacker = cfg.register_agent_type(
        "attacker",
        {
            'width': 1, 'length': 1, 'hp': 1, 'speed': 1,
            'view_range': gw.CircleRange(5), 'attack_range': gw.CircleRange(2),
            'attack_penalty': -0.2, 'damage':0.5, 'kill_reward':1
        })
    defender = cfg.register_agent_type(
        "defender",
        {
            'width': 1, 'length': 1, 'hp': 1, 'speed': 1,
            'view_range': gw.CircleRange(5), 'attack_range': gw.CircleRange(2),
            'attack_penalty': -0.2, 'damage':0.5
        })
    target = cfg.register_agent_type(
        "target",
        {
            'width': 1, 'length': 1, 'hp': 1, 'speed': 0,
            'view_range': gw.CircleRange(4), 'attack_range': gw.CircleRange(0),
            'kill_reward':1, 'damage':0.5
        })

    attacker_group  = cfg.add_group(attacker)
    defender_group = cfg.add_group(defender)
    target_group = cfg.add_group(target)

    a = gw.AgentSymbol(attacker_group, index='any')
    b = gw.AgentSymbol(defender_group, index='any')
    c = gw.AgentSymbol(target_group, index='any')

    cfg.add_reward_rule(gw.Event(a, 'kill', c), receiver=[a, c], value=[1, -1])
    cfg.add_reward_rule(gw.Event(b, 'kill', a), receiver=[b, a], value=[1, -1])
    # cfg.add_reward_rule(gw.Event(c, 'die'), receiver=[b,c], value=[-1,-1])

    return cfg
