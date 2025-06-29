from fastapi import FastAPI
from pydantic import BaseModel
from agents.agentic_workflow import GraphBuilder
from fastapi.responses import JSONResponse
import os



app = FastAPI()

class QueryRequest(BaseModel):
    query:str


@app.post("/query")
def query_travel_agent(query:QueryRequest):
    try:
        print(query)
        graph=GraphBuilder(model_provider="groq")

        react_app=graph()

        png_graph=react_app.get_graph().draw_mermaid_png()

        with open("my_graph_png")as f:
            f.write(png_graph)
        
        print(f"graph saved as 'my_graph.png in {os.getcwd()}")

        #assuming request is a pydenctic object like :{"question":"your text"}
        messages={"messages":[query.question]}

        output = react_app.invoke(messages)

        #if result is a dict with messages:
        if isinstance(output,dict) and "messages" in output:
            final_output=output["messages"][-1].content #last ai reponse
        else:
            final_output=str(output)
    
    except Exception as e:
        return JSONResponse(status_code=500,content={"error":str(e)})