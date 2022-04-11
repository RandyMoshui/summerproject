<?php
// 设置文件头-默认中文编码
header('Content-Type:application/json; charset=utf-8');

// 定义数组
$arr = array();


// 数据库用户名
$user = 'root';
// 数据库密码
$pass = '123456';



try{
    // 使用PDO建立数据库连接
    $dbh = new PDO('mysql:host=192.168.50.131;dbname=cookie_info',$user,$pass);
    // 打印PDO信息
    $count = 0;
    foreach ($dbh->query('select * from 家常菜谱') as $row){
        // echo $row['titles'].PHP_EOL;
        // echo $row['href'].PHP_EOL;
        // 将查询到的数据放入数组中
        $arr[$count] = array('title'=>$row['titles'],'href'=>$row['href']);
        $count = $count + 1;
    }

    // 关闭连接
    $dbh = null;
}catch (PDOException $e){
    echo "Error".$e->getMessage().PHP_EOL;
    die();
}


// 返回json数据
exit(json_encode($arr));
?>