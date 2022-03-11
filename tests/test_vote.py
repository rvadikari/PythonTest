
import pytest


@pytest.mark.parametrize("post_id,dir,expected",[(1,1,201),(2,0,404),(1,0,404)])
def test_create_vote(authorized_client,test_posts,post_id,dir,expected):

    res=authorized_client.post(f"/vote/",json={"post_id":post_id,"dir":dir})
    print(res.json())
    assert res.status_code==expected