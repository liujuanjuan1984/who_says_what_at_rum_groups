# who_says_what_at_rum_groups

rum bot: 从指定的 groups 中搜寻特定 pubkeys 所发布的内容及交互行为，并生成动态转发到指定 group 。

### 部署

0、安装依赖

```sh
pip install mininode
git clone https://github.com/liujuanjuan1984/who_says_what_at_rum_groups
cd who_says_what_at_rum_groups
```

- Quorum [mininode](https://github.com/liujuanjuan1984/mininode)

1、修改 `whosays/config.py`

2、执行 `WhoSays.init_whos_keys()` 搜寻目标作者的 pubkeys ，并人工筛选；也可手动添加

3、执行 `WhoSays().init_profile()` 初始化 bot 的昵称并发布声明

4、持续执行 `WhoSays().send_to_rum()` 转发动态到指定种子网络

### 代码格式化

使用 `isort` 及 [black](https://github.com/psf/black/) 

Install:

```bash
pip install black
pip install isort
```

Format:

```bash
isort .
black -l 120 -t py39 .
```