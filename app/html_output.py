import cherrypy
import os.path
import struct
from jinja2 import Template
import codecs

led_switch=1 
def textfield(switch=''):
        myText = ''
        if switch:
            led_switch = int(switch)             
            myText = " "
        html = """
                       <form action="/action_page.php">
              <label for="fname">First name:</label><br>
              <input type="text" id="fname" name="fname"><br>
              <label for="lname">Last name:</label><br>
              <input type="text" id="lname" name="lname"><br><br>
              <input type="submit" value="Submit">
            </form> 
                """
        return html.format(htmlText=myText)
    
def image(switch=''):
        myText = ''
        if switch:
            led_switch = int(switch)             
            myText = " "
        html = """
                <img id="image" src="/path/to/image.jpg"/>  
                """
        return html.format(htmlText=myText)
        
def button(switch=''):
        myText = ''
        if switch:
            led_switch = int(switch)             
            myText = " "
        html = """
                <button class="button button1">Button</button>
                """
        return html.format(htmlText=myText)
        
def menubar(switch=''):
        myText = ''
        if switch:
            led_switch = int(switch)             
            myText = " "
        html = """
            <<div class="topnav">
              <a class="active" href="####">####</a>
              <a href="####">####</a>
              <a href="####">####</a>
              <a href="####">####</a>
            </div>
                """
        return html.format(htmlText=myText)
        
def sidebar(switch=''):
        myText = ''
        if switch:
            led_switch = int(switch)             
            myText = " "
        html = """
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
                
                <div class="w3-sidebar w3-light-grey w3-bar-block" style="width:25%">
                  <a href="####">####</a>
                  <a href="####">####</a>
                  <a href="####">####</a>
                  <a href="####">####</a>
                </div>
                """
        return html.format(htmlText=myText)

def navbar(switch=''):
        myText = ''
        if switch:
            led_switch = int(switch)             
            myText = " "
        html = """
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
                
                <div class="w3-sidebar w3-light-grey w3-bar-block" style="width:25%">
                  <a href="####">####</a>
                  <a href="####">####</a>
                  <a href="####">####</a>
                  <a href="####">####</a>
                </div>
                """
        return html.format(htmlText=myText)