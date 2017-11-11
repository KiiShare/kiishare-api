package com.kllawesome.app

import com.kllawesome.app.util.coroutineHandler
import io.vertx.core.http.HttpServer
import io.vertx.ext.web.Router
import io.vertx.ext.web.RoutingContext
import io.vertx.ext.web.handler.BodyHandler
import io.vertx.ext.web.handler.StaticHandler
import io.vertx.kotlin.coroutines.CoroutineVerticle
import io.vertx.kotlin.coroutines.awaitResult


class App : CoroutineVerticle() {

    suspend override fun start() {
        // Build Vert.x Web router
        val router = Router.router(vertx)
        router.route().handler(BodyHandler.create())
        router.post("/api/upload").coroutineHandler { ctx -> uploadConfig(ctx) }

        // Start the server
        awaitResult<HttpServer> {
            vertx.createHttpServer()
                    .requestHandler(router::accept)
                    .listen(config.getInteger("http.port", 8080), it)
        }
    }

    suspend fun uploadConfig(ctx: RoutingContext) {
        val jsonBody = ctx.bodyAsJson
        val configName = jsonBody.getString("configTitle")
        val config = jsonBody.getString("config")


        println(config)
        // TODO: Do Stuff
        ctx.response().setStatusCode(200).end("noice")
    }
}
