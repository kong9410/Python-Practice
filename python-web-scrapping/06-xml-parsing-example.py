#06-xml-parsing-example
import xml.etree.ElementTree as elemTree

xmlStr = '''
            <users>
                <user grade="gold">
                    <name>Kim Cheol Soo</name>
                    <age>25</age>
                    <birthday>19940215</birthday>
                </user>
                <user grade="diamond">
                    <name>Kim Yoo Mee</name>
                    <age>21</age>
                    <birthday>19980417</birthday>
                </user>
            </users>
        '''

tree = elemTree.fromstring(xmlStr)
user = tree.find('./user')  #첫번째 user를 검색 후 마침

print(user.tag) #tag name -> user
print(user.attrib) #{'grade' : 'gold'}
print(user.get('grade')) #attr value -> gold

userName = user.find('name') #<name></name> tag
print(userName.text) #Kim Cheol Soo
