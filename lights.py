import json
import requests

class Light:
    baseurl="http://10.130.10.111/api/3QEbijbqAbKxzK-qSdfwHzL0qWOB2Ll1h8cPqfn7"
    lights_url=baseurl + "/lights"
    lights_state_url=baseurl + "/lights/%s/state"
    
    def __init__(self, num, light_name, on, bri):
        self.name = light_name
        self.num = num
        self.on = on
        self.bri = bri
        
    def __repr__(self):
        return "Light#%s<name=%r>" % (self.num, self.name)
    
    def set_state(self, state):
        response = requests.put(
            url=self.lights_state_url % self.num,
            headers={
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({
                "on": state
            })
        )
        
    def set_brightness(self, brightness):
        response = requests.put(
            url=self.lights_state_url % self.num,
            headers={
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({
                "bri": brightness
            })
        )
         
    def turn_on(self):
        self.set_state(True)

    def turn_off(self):
        self.set_state(False)
        
    @classmethod
    def refresh(cls):
        hei = 1
        cls.get_lights()
        
    @classmethod
    def find_light(cls, target_name):
        for light in cls._lights:
            if light.name == target_name:
                return light

    @classmethod
    def get_lights(cls):
        response = requests.get(url=Light.lights_url)
        data = json.loads(response.content)
        lights = []
        for num, light_data in data.items():
            lights.append(Light(
                num,
                light_data['name'],
                light_data['state']['on'],
                light_data['state'].get('bri'),                   
            ))
        cls._lights = lights
        return lights
