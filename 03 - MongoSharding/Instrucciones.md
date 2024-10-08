# ReplicaSet

La idea es primero entender cómo se configura una replica en Mongo, por lo que lo vamos a hacer "a mano" introduciendo todos los comandos uno por uno y revisar el comportamiento.

Siempre utilizando mongo, vamos a ejecutar tres contenedores de mongo y nos vamos a conectar a cada uno en terminales distintas. Luego de realizar este ejercicio, utilizaremos docker compose para automatizar la tarea.

## Paso 1. Descarga de la imagen de mongo

``` bash
docker pull mongo
```

## Paso 2. Generamos una red propia para nuestras instancias de mongo

```
docker network create mongo-replica-1
```

## Paso 3. Ejecutar tres instancias de mongo

Tomen nota del compando con el que ejecutamos mongo en el docker run, le pasamos el argumento con el nombre que le vamos a poner a nuestra réplica.

Noten también el cambio en el número de puerto, de esta forma no hay conflictos con los puertos abiertos en el host

```
docker run \
    -p 30001:27017 \
    --name mongo1 \
    --net mongo-replica-1 \
    mongo:5.0 mongod --replSet replica-1
```

```
docker run \
    -p 30002:27017 \
    --name mongo2 \
    --net mongo-replica-1 \
    mongo:5.0 mongod --replSet replica-1
```

```
docker run \
    -p 30003:27017 \
    --name mongo3 \
    --net mongo-replica-1 \
    mongo:5.0 mongod --replSet replica-1
```

## Paso 4. Ahora tenemos que especificar donde encontrar a los otros nodos
Si lo observan, es suficiente con abrir una terminal en una de las instancias y establecer una configuración con formato de json

```
docker exec -it mongo1 mongo
```
```
db = (new Mongo('localhost:27017')).getDB('test')
test
```


``` json
(config = { 
    "_id" : "replica-1",
    "members" : [
        {
            "_id" : 0,
            "host" : "mongo1:27017"
        },
        {
            "_id" : 1,
            "host" : "mongo2:27017"
        },
        {
          "_id" : 2,
          "host" : "mongo3:27017"
        }
        ]
})
```

```
rs.initiate(config)
```


## Sharding

REvisar el docker compose con todos los servicios y configurar lo siguiente

Configuración para la replica de config servers
``` js
rs.initiate({
    _id: "mongors1conf", 
    configsvr: true, 
    members: [
        { 
            _id : 0, 
            host : "mongocfg1" 
        },
        { 
            _id : 1, 
            host : "mongocfg2" 
        }, 
        { 
            _id : 2, 
            host : "mongocfg3" 
        }
    ]
})
```

``` js
rs.initiate({
    _id : "mongors1", 
    members: [
        { 
            _id : 0, 
            host : "mongors1n1" 
        },
        { 
            _id : 1, 
            host : "mongors1n2" 
        },
        { 
            _id : 2, 
            host : "mongors1n3" 
        }
    ]
})
```

``` js
rs.initiate({
    _id : "mongors2", 
    members: [
        { 
            _id : 0, 
            host : "mongors2n1" 
        },
        { 
            _id : 1, 
            host : "mongors2n2" 
        },
        { 
            _id : 2, 
            host : "mongors2n3" 
        }
    ]
})
```

``` js
rs.initiate({
    _id : "mongors3", 
    members: [
        { 
            _id : 0, 
            host : "mongors3n1" 
        },
        { 
            _id : 1, 
            host : "mongors3n2" 
        },
        { 
            _id : 2, 
            host : "mongors3n3" 
        }
    ]
})
```




Configuración del sharding

``` js
sh.addShard("mongors1/mongors1n1")
sh.addShard("mongors2/mongors2n1")
sh.addShard("mongors3/mongors3n1")
```

creacion de la base de datos:

``` js
sh.enableSharding("travel_social");

sh.shardCollection("travel_social.users", { _id: "hashed" });
sh.shardCollection("travel_social.posts", { user_id: "hashed" });
sh.shardCollection("travel_social.comments", { post_id: "hashed" });
sh.shardCollection("travel_social.likes", { post_id: "hashed" });
sh.shardCollection("travel_social.follows", { user_id: "hashed" });
```



Insertar datos distribuidos uniformemente:

``` js
for (let i = 1; i <= 5000; i++) {
    db.users.insertOne({
        username: 'usuario' + i,
        email: 'usuario' + i + '@example.com',
        password: 'pass' + i,  // Contraseña ficticia
        bio: 'Esta es la biografía del usuario ' + i + ', apasionado de los viajes y aventuras por todo el mundo.'
    });
}



for (let i = 1; i <= 10000; i++) {
    db.posts.insertOne({
        user_id: Math.floor(Math.random() * 5000) + 1,  // Relacionado con un usuario aleatorio
        text: 'Este es el post número ' + i + ' sobre un increíble destino de viaje.',
        photos: ['http://example.com/photo' + i + '.jpg'],
        created_at: new Date()
    });
}


for (let i = 1; i <= 50000; i++) {
    db.comments.insertOne({
        post_id: Math.floor(Math.random() * 10000) + 1,  // Relacionado con un post aleatorio
        user_id: Math.floor(Math.random() * 5000) + 1,  // Relacionado con un usuario aleatorio
        text: 'Este es un comentario número ' + i + ' sobre un post de viajes.',
        created_at: new Date()
    });
}


for (let i = 1; i <= 100000; i++) {
    db.likes.insertOne({
        post_id: Math.floor(Math.random() * 10000) + 1,  // Relacionado con un post aleatorio
        user_id: Math.floor(Math.random() * 5000) + 1,  // Relacionado con un usuario aleatorio
    });
}


for (let i = 1; i <= 5000; i++) {
    db.follows.insertOne({
        user_id: Math.floor(Math.random() * 5000) + 1,  // Usuario que sigue
        topic: 'Destino ' + i  // Tema aleatorio
    });
}
```

Verificar la distribución de los datos:

``` js
db.users.getShardDistribution();
db.posts.getShardDistribution();
db.comments.getShardDistribution();
db.likes.getShardDistribution();
db.follows.getShardDistribution();
```


algunos queries de prueba para los datos:

``` js
db.posts.find({ user_id: 123 });
db.likes.find({ user_id: 5678 }).pretty();
db.likes.find({ post_id: 1234 }).pretty();
```
