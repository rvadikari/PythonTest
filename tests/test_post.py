def test_get_posts(authorized_client,test_posts):
    res=authorized_client.get("/posts/")
    
    assert res.status_code==200

def test_get_post_by_id(authorized_client,test_posts):
    res=authorized_client.get("/posts/1")
    
    assert res.status_code==200

def test_create_post(authorized_client,test_user,test_posts):
    res=authorized_client.post(f"/posts/",json={"title":"newpost","content":"new post content"})
    
    assert res.status_code==201
def test_update_post(authorized_client,test_user,test_posts):
    res=authorized_client.put(f"/posts/1",json={"id":"1","title":"updatedpost","content":"updated post content"})
    assert res.status_code==200
  