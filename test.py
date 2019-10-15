import os
import sys
import unittest
from models import db, Game, Engine, Developer

class DBTestCases(unittest.TestCase):

    #Unit test for games

    def test_source_insert_1(self):
        s = Game(id='42', title = 'Pcaman')
        db.session.add(s)
        db.session.commit()
        r = db.session.query(Game).filter_by(id = '42').one()
        self.assertEqual(str(r.id), '42')
        self.assertEqual(str(r.title), 'Pcaman')
        db.session.query(Game).filter_by(id = '42').delete()
        db.session.commit()

    def test_source_insert_2(self):

        r = db.session.query(Game).filter_by(id = '4754').one()
        self.assertEqual(str(r.id), '4754')
        self.assertEqual(str(r.title), 'Alien: Isolation')



    def test_source_insert_3(self):

        r = db.session.query(Game).filter_by(id = '1887').one()
        self.assertEqual(str(r.id), '1887')
        self.assertEqual(str(r.title), 'Dragon Age: Inquisition')





    #engines
    def test_source_insert_4(self):

        r = db.session.query(Engine).filter_by(id = '2').one()
        self.assertEqual(str(r.id), '2')
        self.assertEqual(str(r.name), 'Frostbite')


    def test_source_insert_5(self):

        r = db.session.query(Engine).filter_by(id = '123').one()
        self.assertEqual(str(r.id), '123')
        self.assertEqual(str(r.name), 'IW Engine')


    def test_source_insert_6(self):

        r = db.session.query(Engine).filter_by(id = '351').one()
        self.assertEqual(str(r.id), '351')
        self.assertEqual(str(r.name), 'Unreal Engine 3')




    #devs
    def test_source_insert_7(self):

        r = db.session.query(Developer).filter_by(id = '438').one()
        self.assertEqual(str(r.id), '438')
        self.assertEqual(str(r.name), 'Infinity Ward')


    def test_source_insert_8(self):

        r = db.session.query(Developer).filter_by(id = '71').one()
        self.assertEqual(str(r.id), '71')
        self.assertEqual(str(r.name), 'Raven Software')
  

    def test_source_insert_9(self):
 
        r = db.session.query(Developer).filter_by(id = '454').one()
        self.assertEqual(str(r.id), '454')
        self.assertEqual(str(r.name), 'EA Sports')



if __name__ == '__main__':
    unittest.main()
