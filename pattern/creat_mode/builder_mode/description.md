### 建造者模式
    建造者模式: 把对象创建的权限放到Builder类.
#### 实现了两种建造者模式
##### 第一种: 
[1. 创建Builder抽象类,然后让具体Builder继承抽象类,具体Builder来创建实体类的细节](./builder.py)

[2. 创建Director类来管理具体Builder的创建细节顺序以及最后返回实体类](./director.py)
    
##### [第二种:](./class_builder.py)

    1. 创建Builder类实现链式编程来初始化属性
    2. 在Builder类中加入一个方法来生成需要的实体类
    3. 修改实体类中的构造器,通过传入的Builder来赋值到实体类的属性