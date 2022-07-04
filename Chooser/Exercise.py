import json

class Exercise(json.JSONEncoder):
    def __init__(self, title, complexity, description, worker):
        self.title = title
        self.complexity = complexity
        self.description = description
        self.worker = worker
        worker.sort()
    
    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    def __repr__(self):
        return f'<Title {self.title}>'

    def to_dict(u):
      dict = {
        "title": u.title,
        "complexity": u.complexity,
        "description": u.description,
        "worker": u.worker
      }
      return dict
