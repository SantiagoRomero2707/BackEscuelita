from ControllerGraphQL.Entity.routes_mutation import Mutation
from ControllerGraphQL.Entity.routes_query import Query
from strawberry.asgi import GraphQL
from fastapi import FastAPI
import strawberry


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQL(schema)
app = FastAPI()
app.add_route("/", graphql_app)
