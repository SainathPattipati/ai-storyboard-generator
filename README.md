# AI Storyboard Generator

Convert text descriptions to visual storyboards — scene composition, character placement, camera direction.

## Features

- Parse scripts into structured scenes
- Apply cinematography composition rules
- Generate camera angles and movements
- Create PDF storyboards
- Export for video production tools

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from src.storyboard.scene_parser import SceneParser
from src.storyboard.composition_engine import CompositionEngine
from src.storyboard.panel_generator import PanelGenerator

parser = SceneParser()
scenes = parser.parse_script("INT. OFFICE - DAY...")

composition = CompositionEngine()
for scene in scenes:
    composed = composition.apply_rules(scene)
    
    generator = PanelGenerator()
    panels = generator.generate(composed)
```

## Cinematography Rules

- Rule of thirds for composition
- Leading lines for viewer guidance
- Depth of field effects
- Character positioning and eyelines

## Dependencies

- langchain >= 0.1.0
- openai >= 0.27.0
- pydantic >= 1.10.0
- reportlab >= 4.0.0
- pillow >= 9.0.0

## License

MIT License
