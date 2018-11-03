# MAgent

## 目录结构

```bash
data/
	figure/   		#原项目文档所用图像
	font_8*8/ 		#提供像素样式？
	pursuit_model/ 	#保存已训练好的predator/prey模型
doc/			#原文档，包含（简陋的）使用指南
examples/		#训练文件以及展示文件示例
python/
	magent/			#封装好的magent模块，使用示例见MAgent/examples/
		builtin/		
			config/			#默认配置文件，包含pursuit、forest、double_attack、battle
			mx_model/		#用深度学习库MXnet实现的Advantage actor critic, base model 与dqn
			tf_model/		#用tensorflow实现的advantage actor critic, base model与dqn
			rule_model/		#在实际训练中只用到了random actor模板用于初始化
				random.py		# an agent that takes random action
				runaway.py		# deprecated
				rush.py			# deprecated
				rushgather.py	# deprecated
		renderer/				# 似乎是用于与Pygame衔接，以动态显示训练效果
		discrete_snake.py 		# deprecated(另一个游戏环境模板)
		environment.py 			# 环境基本类（应用于discrete_snake/gridWorld)
		gridworld.py			# Gridworld游戏环境设置接口（用于在训练前设置参数）
		model.py				# Agent所用model的基本模板
scripts/		# 根目录下的一系列文件用于绘制训练过程中log记录的各参数曲线
	test/		# 一系列执行训练任务的模板示例
    plot_heat.py		
    plot_log.py
    plot_many.py
    plot_reward.py
    plot.py
    rename.py
    tournament.py
src/			# 用c++实现的游戏引擎
zh_doc/			# 我写的中文文档XD
```



## 默认模型配置

### pursuit(追捕)

##### param:

|                | predator | prey             |
| -------------- | -------- | ---------------- |
| size           | 2*2      | 1*1              |
| hp             | 1        | 1                |
| speed          | 1        | 1.5              |
| view_range     | 半径为5px   | 半径为4px           |
| attack_range   | 半径为4px   | 半径为0px（无法attack） |
| attack_penalty | -0.2     | 无                |

##### config：

``python/magent/builtin/config/pursuit.py``

### forest(丛林)

##### param:

|                   | tiger  | deer             |
| ----------------- | ------ | ---------------- |
| size              | 1*1    | 1*1              |
| hp                | 10     | 5                |
| speed             | 1      | 1                |
| view_range        | 半径为4px | 半径为1px           |
| attack_range      | 半径为1px | 半径为0px（无法attack） |
| kill_supply(????) | 0      | 8                |
| attack_penalty    | -0.1   | 无                |
| step_reward       | 1      |                  |
| damage            | 3      | 0                |
| step_recover      | -0.5   | 0.2              |

##### config:

``python/magent/builtin/config/forest.py``

### double-attack(丛林II)

##### param：

基本同forest模型，两组tiger，一组deer

##### config：

``python/magent/builtin/config/double_attack.py``

### battle(战争)

##### param:

两组 *small* 相互攻击

|                | small        |
| -------------- | ------------ |
| size           | 1*1          |
| hp             | 10           |
| speed          | 2            |
| view_range     | radius=5px   |
| attack_range   | radius=1.5px |
| damage         | 2            |
| step_recover   | 0.1          |
| step_reward    | -0.005       |
| kill_reward    | 5            |
| dead_penalty   | -0.1         |
| attack_penalty | -0.1         |

##### config：

python/magent/builtin/config/double_attack.py