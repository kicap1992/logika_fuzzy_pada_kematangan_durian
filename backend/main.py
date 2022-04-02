# from typing import Optional
import json
import os
from fastapi import FastAPI, Form, UploadFile , File , Request,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fuzzy import fuzzy
# import asyncio
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# create the fastapi api
@app.get("/")
async def read_root():
    dataset = await fuzzy("ambil_dataset")
    # dataset.update({"image_usia":FileResponse(image_usia)})
    return dataset

# create post request
@app.post("/")
async def read_root_post(request: Request):
    body = await request.form()
    if body:
        # check if body['data'] is not empty and not None
        if body['data'] is not None and body['data'] != "":
            json_data = json.loads(body['data'])

            datanya = await fuzzy("load_fuzzy", json_data['usia'], json_data['berat'], json_data['keliling'], json_data['ukuran_batang'], json_data['jarak_duri'])
            # print(datanya)
            return {"ket": datanya}
        else:
            raise HTTPException(status_code=400, detail="data is empty")
    else:
        # print("ko")
        raise HTTPException(status_code=404, detail="error")
    # return {"message": "sini post datanya"}

# creata a image get
@app.get("/image/{image_name}")
async def read_image(image_name: str):
    file_path = os.path.join("", image_name+'.png')
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")
    # image = await FileResponse(image_name+".png")
    # return image


# create post method /fuzzy with form data and return the data
# @app.post("/fuzzy")
# async def read_item(nama: str = Form(...),
#                     umur: int = Form(...),
#                     alamat: str = Form(...),
#                     foto : UploadFile = File(...)):
#     return {"nama": nama, "umur": umur, "alamat": alamat, "foto": foto}
    