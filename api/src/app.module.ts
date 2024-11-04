import { Module } from "@nestjs/common";
import { AppController } from "./app.controller";
import { AppService } from "./app.service";
import { TypeOrmModule } from "@nestjs/typeorm";

@Module({
	imports: [
		TypeOrmModule.forRoot({
			type: "mysql",
			host: "mysql", // O nome do container do MySQL
			port: 3306, // A porta padrão do MySQL
			username: "admin",
			password: "root",
			database: "rocketseat-db",
			entities: [], // Adicione suas entidades aqui
			synchronize: true,
		}),
	],
	controllers: [AppController],
	providers: [AppService],
})
export class AppModule {}
