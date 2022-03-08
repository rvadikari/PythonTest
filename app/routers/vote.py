from operator import mod
from fastapi import Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from .. import models,schemas,database,oauth2

router=APIRouter(
    prefix="/vote",
    tags=["Vote"]
)
@router.post("/",status_code=status.HTTP_201_CREATED)
def create_vote(vote:schemas.Vote,db:Session=Depends(database.get_db),current_user:int = Depends(oauth2.get_current_user)):
    post=db.query(models.Post).filter(models.Post.id==vote.post_id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {vote.post_id} is not found')
    
    vote_db= db.query(models.Vote).filter(models.Vote.post_id==vote.post_id,models.Vote.user_id==current_user.id)
    found_vote=vote_db.first()
    
    if vote.dir==1:
        if found_vote:
             raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'User with id {current_user.id} already voted')
    
        vote_new=models.Vote(post_id=vote.post_id,user_id=current_user.id)
        db.add(vote_new)
        db.commit()
        return{"message":"Voting has been done successfully"}
    else:
       if not found_vote:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'vote with {vote.post_id} is not Found')
       vote_db.delete(synchronize_session=False)
       db.commit()
       return{"message":"Voting has been removed successfully"}


