import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/api/users/me')
async def get_users_me():
    return {
        'result': 'True',
        'user': {
            'id':1,
            'name': 'Mikhail Arkhipychev',
            'followers':[{'id':2, 'name':'Maria Arkhipycheva'}],
            'following': [{'id':2, 'name': 'Maria Arkhipycheva'}],

        },
    }

# if __name__ == '__main__':
#     # uvicorn.run('main:app', host='0.0.0.0', port=8000)