import magent


def get_config(map_size):
    gw = magent.gridworld
    cfg = gw.Config()

    cfg.set({"map_width": map_size, "map_height": map_size})

    killer = cfg.register_agent_type(
        "killer",
        {
            'width': 1, 'length': 1, 'hp': 1, 'speed': 1,
            'view_range': gw.CircleRange(5), 'attack_range': gw.CircleRange(2),
            'attack_penalty': -0.2
        })

    guard = cfg.register_agent_type(
        "guard",
        {
            'width': 1, 'length': 1, 'hp': 1, 'speed': 1,
            'view_range': gw.CircleRange(5), 'attack_range': gw.CircleRange(2),
            'attack_penalty': -0.2
        })

    king = cfg.register_agent_type(
        "king",
        {
            'width': 1, 'length': 1, 'hp': 1, 'speed': 0,
            'view_range': gw.CircleRange(5), 'attack_range': gw.CircleRange(0),
        })

    killer_group  = cfg.add_group(killer)        
    guard_group = cfg.add_group(guard)           
    king_group = cfg.add_group(king)            

    a = gw.AgentSymbol(killer_group, index='any')    
    b = gw.AgentSymbol(guard_group, index='any')      
    c = gw.AgentSymbol(king_group, index='any')     

    cfg.add_reward_rule(gw.Event(a, 'attack', b), receiver=[a, b], value=[1, -1])
    cfg.add_reward_rule(gw.Event(a, 'attack', c), receiver=[a, b], value=[100, -100])
    cfg.add_reward_rule(gw.Event(b, 'attack', a), receiver=[a, b], value=[-1, 1])
    cfg.add_reward_rule(gw.Event(b, 'attack', c), receiver=[a, b], value=[100, -100])

    return cfg
