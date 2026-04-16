from crewai import Crew, Process, Task
from agents.designer_agent import designer_agent
from agents.developer_agent import developer_agent
from config.settings import settings

def create_website_crew():
    """Create and configure the website builder crew"""
    
    # Task 1: Design specifications
    design_task = Task(
        description="""Based on the user's requirements, create a detailed design specification including:
        1. Layout structure and wireframe description
        2. Color scheme (primary, secondary, accent colors with hex codes)
        3. Typography (font families, sizes, weights for different elements)
        4. Component styles (buttons, cards, navigation, etc.)
        5. Responsive breakpoints strategy
        6. Special design elements or animations
        
        Provide the output in a structured format that the developer can use.""",
        agent=designer_agent,
        expected_output="Detailed design specifications with colors, typography, layout, and styling guidelines"
    )
    
    # Task 2: Code generation
    code_task = Task(
        description="""Based on the design specifications from the designer, generate a complete, 
        production-ready HTML/CSS/JavaScript website. 
        
        Requirements:
        1. Write complete, valid HTML5 code
        2. Include responsive CSS using Grid and Flexbox
        3. Add interactive features with vanilla JavaScript
        4. Ensure semantic HTML structure
        5. Optimize for performance
        6. Include proper meta tags for SEO
        7. Make it mobile-friendly
        
        Provide the complete code as a single HTML file that can be opened in a browser.""",
        agent=developer_agent,
        expected_output="Complete HTML file with embedded CSS and JavaScript ready to be deployed"
    )
    
    crew = Crew(
        agents=[designer_agent, developer_agent],
        tasks=[design_task, code_task],
        process=Process.sequential,
        verbose=settings.VERBOSE_MODE
    )
    
    return crew

def build_website(user_requirements: str) -> dict:
    """
    Build a website based on user requirements
    
    Args:
        user_requirements: User's description of desired website
        
    Returns:
        Dictionary containing design specs and HTML code
    """
    crew = create_website_crew()
    
    result = crew.kickoff(
        inputs={
            "user_requirements": user_requirements,
            "project_name": user_requirements.split()[0] if user_requirements else "Website"
        }
    )
    
    return {
        "status": "success",
        "result": result,
        "requirements": user_requirements
    }
