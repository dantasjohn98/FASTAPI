from dataclasses import asdict

from sqlachemy import select

from fastapi_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='alice',
            email='test@test',
            password='secret',
        )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))
    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'email': 'test@test',
        'password': 'secret',
        'created_at': time,
    }
