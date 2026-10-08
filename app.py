from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/Fake_epm_testing")
def get_fake_data():
    return [
        {
            "id":1,
            "name":"John Doe"
        },
        {
            "id":1,
            "name":"John Doe"
        },
                
        {
            "id":1,
             "name":"John Doe"
                        
        }
    ]

@app.post("/data_push")
def add_data(data:dict):
    budget_data.append(data)
    return{
        "data_append":"dada added Successfully",
        "data":data
    }
