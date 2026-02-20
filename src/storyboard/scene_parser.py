"""Parse scripts into scenes."""
from typing import List
from dataclasses import dataclass

@dataclass
class Scene:
    """Parsed scene."""
    description: str
    characters: List[str]
    camera_notes: str

class SceneParser:
    """Parse script descriptions."""
    
    def parse_script(self, script_text: str) -> List[Scene]:
        """Parse script into scenes."""
        return [Scene("INT. OFFICE - DAY", ["ALICE", "BOB"], "")]
