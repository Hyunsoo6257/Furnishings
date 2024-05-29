from flask import Blueprint
from . import db
from .models import Category, Product, Order
import datetime

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# function to put some seed data in the database
@admin_bp.route('/dbseed')
def dbseed():
    category1 = Category(name='Living', image='../static/img/Living_main.jpg', \
        description='''Living furniture''')
    category2 = Category(name='Outdoor', image='../static/img/Outdoor_main.jpg', \
        description='''Outdoor_furniture''')
    category3 = Category(name='Lighting', image='../static/img/Lighting_main.jpg', \
        description='''LIGHTING_FURINITURE''')
      
    try:
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.commit()
    except:
        return 'There was an issue adding the cities in dbseed function'

    p1 = Product(category_id=category1.id, image='../static/img/Living_1.jpg', price=59.99,\
        date=datetime.datetime(2023, 5, 17),\
        name='Cuddle koalas',\
        description= 'Lone Pine Koala Sanctuary is the world\'s first and largest koala sanctuary and is home to more than 130 koalas. Hand-feed their kangaroos and wild lorikeets, be entertained by a platypus or - best of all - get cuddly with a beautiful koala. Duration 0900-1400 (5hrs), begins at entrance to Koala Plaza') 
    p2 = Product(category_id=category1.id, image='../static/img/Living_2.jpg', price=100.50,\
        date=datetime.datetime(2023, 2, 1),\
        name='Hand-feed kangaroo',\
        description= 'Get up close and personal with Australia\'s favourite wildlife and tick two items off your bucket list with a trip to Lone Pine Koala Sanctuary. Lone Pine is only 40 minutes from the CBD by bus and you\'ll be cuddling up to koalas and hand-feeding kangaroos in no time. Don\'t forget the selfie! Duration 0900-1300 (4hrs), begins at entrance to Kanga Plaza.')
    p3 = Product(category_id=category1.id, image='../static/img/Living_3.jpg', price=180.50,\
        date=datetime.datetime(2023, 3, 10),\
        name='Sand island adventure',\
        description= 'You don\'t have to travel to the far north to see Australia\'s bustling reef and sea life. Take a short ferry ride from the Port of Brisbane and you\'ll find yourself at Moreton Island, a tropical sand island with crystal-clear coastal water, lakes and incredible snorkelling at the historic Tangalooma Wrecks. You\'ll want your GoPro to take some incredible underwater snaps. Duration 0900-1700 (8hrs), begins at entrance to Transit Centre.')
    p4 = Product(category_id=category1.id, image='../static/img/Living_4.jpg', price=99.99,\
        date=datetime.datetime(2023, 8, 1),\
        name='Whale watching',\
        description= 'From June to November, Whale Watching Tours inc. runs daily cruises for those who want to witness the incredible acrobatics of the southern humpback whale. More than 20,000 whales migrate through every winter. Tickets for the five-hour cruise through Moreton Bay are good value and include guaranteed whale sightings. Duration 1300-1800 (5hrs), begins at entrance to Port Street.')                
    p5 = Product(category_id=category2.id, image='../static/img/Outdoor_1.jpg', price=49.00,\
        date=datetime.datetime(2023, 4, 20),\
        name='Trek around the national park',\
        description= 'Forget the outback and take in the green scene. While most international visitors picture red dirt when they think of Australia, you\'re more likely to find yourself surrounded by lush greenery than outback desert. Take the opportunity to check out local fauna and flora at the national parks, as close as 20 minutes from the CBD. Did we mention our parks have drop-bears? Must bring sunblock. Duration 1000-1300 (3hrs), begins at entrance to Forrest Car Park.')
    p6 = Product(category_id=category2.id, image='../static/img/Outdoor_2.jpg', price=250.99,\
        date=datetime.datetime(2024, 1, 2),\
        name='Island adventure',\
        description= 'The world\'s biggest sand island is just a few hours away. Heritage-listed Big Sandy Island has more than 100 freshwater lakes, pristine water and white-sand beaches. There\'s many ways to explore the island but the most fun is by four-wheel-drive. Join a tour such as the Dingos Resort tag-along four-wheel drive tour, where you can drive yourself and make friends along the way. Duration 0600-1600 (11hrs), begins at entrance to Ferry Road.')
    p7 = Product(category_id=category2.id, image='../static/img/Outdoor_3.jpg', price=120.00,\
        date=datetime.datetime(2023, 11, 1),\
        name='Freshwater swimming holes',\
        description= 'You can\'t come to Australia without enjoying the abundant inland lakes, falls and swimming holes. There\'s almost too many to choose from. Check out Visit our must-swim spots. Duration 0900-1200 (3hrs), begins at entrance to River Park.')
    p8 = Product(category_id=category2.id, image='../static/img/Outdoor_4.jpg', price=60.00,\
        date=datetime.datetime(2023, 4, 1),\
        name='Cruise our wonderful river',\
        description= 'Jump on board a CityCat  or ride our private City Cab to explore the city by ferry. CityCats run between the city and various points of interest all the way around to killer bay. Duration 1000-1200 (2hrs), begins at entrance to CBD Ferry Stop.')
    p9 = Product(category_id=category3.id, image='../static/img/Light_1.jpg', price=189.99,\
        date=datetime.datetime(2023, 5, 17),\
        name='Go chasing waterfalls, waterholes and lakes',\
        description= 'We\'re all about the aquatic life over here in Oz, and you can be too. Take a short trip into the coast and hinterland to discover an abundance of natural waterfalls, waterholes and lakes. You are going to love the diversity we will show you. Duration 0800-1700 (9hrs), begins at entrance Bush Station.')
    p10 = Product(category_id=category3.id, image='../static/img/Light_2.jpg', price=89.95,\
        date=datetime.datetime(2023, 6, 19),\
        name='Climb to the top of the City Bridge',\
        description= 'Get your own city skyline pic when you climb the City Bridge, right here in the CBD. The City Bridge Adventure Climb is one of only three bridge climbs in the world and shows off spectacular city and river views. Twilight is the best time to climb. Free use of safety equipment. Duration 1800-2100 (3hrs), begins at bottom of CBD Climb Inc Office.')
    p11 = Product(category_id=category3.id, image='../static/img/Light_3.jpg', price=45.99,\
        date=datetime.datetime(2020, 2, 24),\
        name='Ride the City Wheel',\
        description= 'Enjoy city views without the climb in the air-conditioned comfort of the City Wheel. Every city has its vantage point and for ours, this is it! Ride at night to see the city light up. Duration 1800-2100 (3hrs), begins at bottom of CBD Wheel Inc Booth.')
    p12 = Product(category_id=category3.id, image='../static/img/Light_4.jpg', price=49.99,\
        date=datetime.datetime(2023, 10, 10),\
        name='Sunrise at Mt High-er',\
        description= 'The official city Lookout at Mt High-er is a heritage-listed site boasting panoramic views of the outer region. This is a definite city bucket list item for locals and travellers alike – and yes, it\'s worth the 4am alarm. Duration 0400-0900 (5hrs), begins at High-er visitor centre.')
    

    try:
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.add(p6)
        db.session.add(p7)
        db.session.add(p8)
        db.session.add(p9)
        db.session.add(p10)
        db.session.add(p11)
        db.session.add(p12)
        db.session.commit()
    except:
        return 'There was an issue adding a product in dbseed function'

    return 'DATA LOADED'