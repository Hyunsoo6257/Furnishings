from flask import Blueprint
from . import db
from .models import Category, Product
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
        description='''Lighting furniture''')
      
    try:
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.commit()
    except:
        return 'There was an issue adding the categories in dbseed function'

    p1 = Product(category_id=category1.id, image='../static/img/Living_1.jpg',color='white',price=59.99,\
        date=datetime.datetime(2023, 5, 17),\
        name='CRATE LOW TABLE',\
        description= 'Initially designed to make use of surplus wooden shipping crates by Dutch architect and designer Gerrit Rietveld in 1934, the Crate Collection has been relaunched in a Rietveld Originals x HAY collaboration. Made with respect for the original design, the Crate Low Table shares the same precisely balanced proportions and transparent') 
    p2 = Product(category_id=category1.id, image='../static/img/Living_2.jpg',color='yellow', price=100.50,\
        date=datetime.datetime(2023, 2, 1),\
        name='REY STOOL',\
        description= 'Based on the original Rey Collection designed by Swiss designer Bruno Rey in 1971, HAY has teamed up with Dietiker to relaunch the Rey Stool. Featuring Dietiker’s unique screwless wood-to-metal connection, the iconic stool has an uncluttered silhouette with angled legs that balance the distinctively rounded edges.')
    p3 = Product(category_id=category1.id, image='../static/img/Living_3.jpg',color='white', price=180.50,\
        date=datetime.datetime(2023, 3, 10),\
        name='REY COFFEE TABLE',\
        description= 'Based on the original Rey Collection designed by Swiss designer Bruno Rey in 1971, HAY has teamed up with Dietiker to relaunch the Rey Coffee Table. Featuring Dietiker’s unique screwless wood-to-metal connection, the iconic table has an uncluttered silhouette with angled legs that balance the distinctively rounded edges.')
    p4 = Product(category_id=category1.id, image='../static/img/Living_4.jpg', color='white',price=99.99,\
        date=datetime.datetime(2023, 8, 1),\
        name='QUILTON SOFA COMBINATION',\
        description= 'Described by the designers as a ‘quilted landscape sofa system’, Quilton serves as a central platform for living, working, socializing and relaxing. Offering a wide assortment of different modules, Doshi Levien’s multi-functional sofa provides the flexibility of a modular system with generous dimensions and sculpted forms.')                
    p5 = Product(category_id=category2.id, image='../static/img/Outdoor_1.jpg', color='white',price=49.00,\
        date=datetime.datetime(2023, 4, 20),\
        name='PALISSADE SUN LOUNGE',\
        description= 'Introducing the newest design in the Palissade collection, the Sun Lounge. Palissade is a collection of outdoor furniture designed by Ronan and Erwan Bouroullec for HAY. The collection was designed to fit a wide variety of environments: cafés, restaurants, gardens, terraces and balconies.')
    p6 = Product(category_id=category2.id, image='../static/img/Outdoor_2.jpg', color='black',price=250.99,\
        date=datetime.datetime(2024, 1, 2),\
        name='PALISSADE DINING BENCH',\
        description= 'Palissade is a collection of outdoor furniture designed by Ronan and Erwan Bouroullec for HAY. The collection was designed to fit a wide variety of environments: cafés, restaurants, gardens, terraces and balconies. The construction allows a wide range of typologies with a common formal language.')
    p7 = Product(category_id=category2.id, image='../static/img/Outdoor_3.jpg', color='green',price=120.00,\
        date=datetime.datetime(2023, 11, 1),\
        name='HEE LOUNGE',\
        description= 'With its wide, welcoming seat and low height, Hee Lounge is definitely the most laid-back model in the Hee series. Although the elemental design is manifested here in more relaxed proportions, it still retains the same light, understated aesthetics and functional properties as the rest of the family.')
    p8 = Product(category_id=category2.id, image='../static/img/Outdoor_4.jpg', color='green',price=60.00,\
        date=datetime.datetime(2023, 4, 1),\
        name='ELEMENTAIRE CHAIR',\
        description= 'With Élémentaire, Ronan and Erwan Bouroullec set out to create a chair that is both aesthetically and physically balanced. A mélange of years of work and experience, Élémentaire uses the latest technology to create a chair that is robust enough to be a long-lasting object while still appearing delicate.')
    p9 = Product(category_id=category3.id, image='../static/img/Light_1.jpg', color='white',price=189.99,\
        date=datetime.datetime(2023, 5, 17),\
        name='CLOCHE TABLE LAMP',\
        description= 'Cloche is a table top lamp providing a directional light. Its black powder coated arm and off-set cast iron base creates a visual imbalance, resembling the suspension of a traditional dining cloche.')
    p10 = Product(category_id=category3.id, image='../static/img/Light_2.jpg', color='white',price=89.95,\
        date=datetime.datetime(2023, 6, 19),\
        name='APEX TABLE LAMP',\
        description= 'Taking cues from the classic Banker’s Light, British designer John Tree merged archetypal references with his contemporary, colourful sensibility to create the Apex Lamp collection. The folded steel shades create a peaked roofline silhouette, providing the inspiration behind the series’ name as well as offering a graphic contrast to the chrome-plated bases. ')
    p11 = Product(category_id=category3.id, image='../static/img/Light_3.jpg', color='yellow',price=45.99,\
        date=datetime.datetime(2020, 2, 24),\
        name='MATIN TABLE LAMP',\
        description= 'The Matin table lamp offers a contemporary yet poetic design, with a construction that combines visual delicacy with physical robustness. It consists of a steel wire bent frame finished in polished brass with matte black hardware, and is paired with a pleated cotton shade in a variety of vibrant colours.')
    p12 = Product(category_id=category3.id, image='../static/img/Light_4.jpg', color='white',price=49.99,\
        date=datetime.datetime(2023, 10, 10),\
        name='BONBON LAMP',\
        description= 'Inspired by her drawings, Ana Kraš’ Bonbon Lamps are hand-woven using an original weaving technique to create textured, one-of-a-kind pieces. In her lampshade collaboration with HAY, she uses the same idea of wrapping cotton-wool yarn around powder-coated steel frames to create individual lampshades that vary slightly in their appearance and texture.')
    

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