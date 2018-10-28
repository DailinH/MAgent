# MAgent文档

## 目录结构

```markdown
data/
	figure/   		#原项目文档所用图像
	font_8*8/ 		#提供像素样式？
	pursuit_model/ 	#保存已训练好的predator/prey模型
doc/			#原文档，包含（简陋的）使用指南
examples/		#训练文件以及展示文件示例
python/
	magent/			#封装好的magent模块，使用示例见MAgent/examples/
		builtin/		#
			config/			#默认配置文件，包含pursuit、forest、double_attack、battle
			mx_model/
			rule_model/
			tf_model/
		renderer/	
		discrete_snake.py #
scripts/
src/
zh_doc/			#我写的中文文档XD
```



## 默认模型

### pursuit(追捕)

|                | predator  | prey                    |
| -------------- | --------- | ----------------------- |
| size           | 2*2       | 1*1                     |
| hp             | 1         | 1                       |
| speed          | 1         | 1.5                     |
| view_range     | 半径为5px | 半径为4px               |
| attack_range   | 半径为4px | 半径为0px（无法attack） |
| attack_penalty | -0.2      | 无                      |

##### config：

``python/magent/builtin/config/pursuit.py``

##### agent:

* predator: 2*2px
* prey: 1*1px

##### reward: 

predator攻击prey的时候，predator加分、prey减分

### forest(丛林)

|                   | tiger     | deer                    |
| ----------------- | --------- | ----------------------- |
| size              | 1*1       | 1*1                     |
| hp                | 10        | 5                       |
| speed             | 1         | 1                       |
| view_range        | 半径为4px | 半径为1px               |
| attack_range      | 半径为1px | 半径为0px（无法attack） |
| kill_supply(????) | 0         | 8                       |
| attack_penalty    | -0.1      | 无                      |
| step_reward       | 1         |                         |
| damage            | 3         | 0                       |
| step_recover      | -0.5      | 0.2                     |



##### config:

``python/magent/builtin/config/forest.py``

##### agent:

* deer: 1*1px，生命值5
* tiger: 1*1px，生命值10

##### reward:

