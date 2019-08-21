from sqlalchemy import desc

from lib.util_sqlalchemy import ResourceMixin
from fakefacts.extensions import db, marshmallow


class Fact(ResourceMixin, db.Model):
    __tablename__ = 'facts'
    id = db.Column(db.Integer, primary_key=True)

    # Relationships.
    user_id = db.Column(db.Integer, db.ForeignKey('users.id',
                                                  onupdate='CASCADE',
                                                  ondelete='CASCADE'),
                        index=True, nullable=False)
    user = db.relationship('User')

    message = db.Column(db.String(200))

    @classmethod
    def latest(cls, limit):
        """
        Return the latest X facts.

        :type limit: int
        :return: SQLAlchemy result
        """
        return Fact.query.order_by(desc(Fact.created_on)).limit(limit).all()

    @classmethod
    def from_community(cls, limit):
        """
        Return the latest X facts along with the username of who posted it.

        :type limit: int
        :return: SQLAlchemy result
        """
        community_facts = Fact.latest(limit)

        data = []

        for fact in community_facts:
            fact = {
                'created_on': fact.created_on,
                'message': fact.message,
                'username': fact.user.username
            }

            data.append(fact)

        return data
