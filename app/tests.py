import os
import sys
import unittest
from models import db, Game, Engine, Developer

class DBTestCases(unittest.TestCase):

    #Unit test for games

    def test_source_insert_1(self):
        s = Game(id='2033', title = 'Call of Duty: Ghosts')
        db.session.add(s)
        db.session.commit()
        r = db.session.query(Game).filter_by(id = '2033').one()
        self.assertEqual(str(r.id), '2033')
        self.assertEqual(str(r.title), 'Call of Duty: Ghosts')
        db.session.query(Game).filter_by(id = '2033').delete()
        db.session.commit()

    def test_source_insert_2(self):
        s = Game(id='4754', title = 'Alien: Isolation')
        db.session.add(s)
        db.session.commit()
        r = db.session.query(Game).filter_by(id = '4754').one()
        self.assertEqual(str(r.id), '4754')
        self.assertEqual(str(r.title), 'Alien: Isolation')
        db.session.query(Game).filter_by(id = '4754').delete()
        db.session.commit()


    def test_source_insert_3(self):
        s = Game(id='1887', title = 'Dragon Age: Inquisition')
        db.session.add(s)
        db.session.commit()
        r = db.session.query(Game).filter_by(id = '1887').one()
        self.assertEqual(str(r.id), '1887')
        self.assertEqual(str(r.title), 'Dragon Age: Inquisition')
        db.session.query(Game).filter_by(id = '1887').delete()
        db.session.commit()





    def test_source_insert_4(self):
        s = Engine(id='2', name = 'Frostbite')
        db.session.merge(s)
        db.session.commit()
        r = db.session.query(Engine).filter_by(id = '2').one()
        self.assertEqual(str(r.id), '2')
        self.assertEqual(str(r.name), 'Frostbite')
        db.session.query(Engine).filter_by(id = '2').delete()
        db.session.commit()

    def test_source_insert_5(self):
        s = Engine(id='123', name = 'IW Engine')
        db.session.merge(s)
        db.session.commit()
        r = db.session.query(Engine).filter_by(id = '123').one()
        self.assertEqual(str(r.id), '123')
        self.assertEqual(str(r.name), 'IW Engine')
        db.session.query(Engine).filter_by(id = '123').delete()
        db.session.commit()

    def test_source_insert_6(self):
        s = Engine(id='351', name = 'Unreal Engine 3')
        db.session.merge(s)
        db.session.commit()
        r = db.session.query(Engine).filter_by(id = '351').one()
        self.assertEqual(str(r.id), '351')
        self.assertEqual(str(r.name), 'Unreal Engine 3')
        db.session.query(Engine).filter_by(id = '351').delete()
        db.session.commit()




    def test_source_insert_7(self):
        s = Developer(id='438', name = 'Infinity Ward')
        db.session.add(s)
        db.session.commit()
        r = db.session.query(Developer).filter_by(id = '438').one()
        self.assertEqual(str(r.id), '438')
        self.assertEqual(str(r.name), 'Infinity Ward')
        db.session.query(Developer).filter_by(id = '438').delete()
        db.session.commit()

    def test_source_insert_8(self):
        s = Developer(id='71', name = 'Raven Software')
        db.session.add(s)
        db.session.commit()
        r = db.session.query(Developer).filter_by(id = '71').one()
        self.assertEqual(str(r.id), '71')
        self.assertEqual(str(r.name), 'Raven Software')
        db.session.query(Developer).filter_by(id = '71').delete()
        db.session.commit()

    def test_source_insert_9(self):
        s = Developer(id='454', name = 'EA Sports')
        db.session.add(s)
        db.session.commit()
        r = db.session.query(Developer).filter_by(id = '454').one()
        self.assertEqual(str(r.id), '454')
        self.assertEqual(str(r.name), 'EA Sports')
        db.session.query(Developer).filter_by(id = '454').delete()
        db.session.commit()

if __name__ == '__main__':
    unittest.main()
