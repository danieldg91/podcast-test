import yaml
import xml.etree.ElementTree as xml_tree

# Creates feed according to RSS FEED standard: https://help.apple.com/itc/podcasts_connect/#/itcbaf351599

with open ('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file) #safeloads (verifies correct file uploading) into 'yaml_data' w. yaml command from module
    #creating an xml tree
    rss_element = xml_tree.Element('rss', {
        'version':'2.0', 
        'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd', 
        'xmlns:content':'http://purl.org/rss/1.0/modules/content/'
    }) 

#channel goes inside the rss element, this only creates a tag
channel_element = xml_tree.SubElement(rss_element, 'channel') 

#link holds github page url (Repo > Settings > Pages)
link_prefix = yaml_data['link']

#inside the channel tag create a title tag to write the contents from the feed.yaml file
xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_element, 'format').text = yaml_data['format']
xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel_element, 'itunes:author').text = yaml_data['author']
xml_tree.SubElement(channel_element, 'description').text = yaml_data['description']
xml_tree.SubElement(channel_element, 'itunes:image', {'href': link_prefix + yaml_data['image']}) #holds data in attributes.
xml_tree.SubElement(channel_element, 'language').text = yaml_data['language']
xml_tree.SubElement(channel_element, 'link').text = link_prefix
xml_tree.SubElement(channel_element, 'itunes:category', {'text': yaml_data['category']}) #also holds data in attributes.

#Create loop for items
for item in yaml_data['item']:
    item_element = xml_tree.SubElement(channel_element, 'item')
    xml_tree.SubElement(item_element, 'title').text 

#prep built element by feeding into output tree
output_tree = xml_tree.ElementTree(rss_element)
#...and write to external file with xml tag at the top and UTF output format
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)  
 