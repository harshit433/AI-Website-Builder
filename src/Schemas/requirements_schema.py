from typing import Any, List, Dict, Optional, Callable
from pydantic import BaseModel, Field, ConfigDict, AliasPath, AliasChoices

class APIIntegration(BaseModel):
    name: str
    endpoint_url: str
    authentication_type: str
    rate_limit: Optional[int] = None
    response_time_sla: Optional[float] = None
    required_params: Dict[str, str] = Field(default_factory=dict)

class UIComponentStyle(BaseModel):
    font_family: str = Field(default="Arial, sans-serif")
    font_sizes: Dict[str, int] = Field(default_factory=lambda: {
        "title": 24,
        "subtitle": 20,
        "body": 16,
        "small": 12
    })
    color_palette: Dict[str, str] = Field(default_factory=lambda: {
        "primary": "#3498db",
        "secondary": "#2ecc71",
        "background": "#ffffff",
        "text": "#333333"
    })

    model_config = ConfigDict(
        validate_assignment = True,
        extra = 'ignore'
    )

class PageLayout(BaseModel):
    type: str = Field(default="grid", description="Layout type (e.g., grid, flexbox, custom)")
    columns: int = Field(default=12)

class NavigationMenuItem(BaseModel):
    label: str
    href: str
    icon: Optional[str] = None
    children: Optional[List['NavigationMenuItem']] = None


class NavigationMenu(BaseModel):
    menu_items: List[NavigationMenuItem]
    navigation_type: str = Field(default="top_bar", description="Top bar, sidebar, hamburger, etc.")
    active_indicator: Optional[str] = None

class PageRequirements(BaseModel):
    name: str
    url_path: str
    page_type: str = Field(default="content", description="landing, dashboard, profile, etc.")
    layout: PageLayout = Field(default_factory=PageLayout)
    components: List[str] = Field(default_factory=list)

class FeatureRequirement(BaseModel):
    name: str
    description: str
    priority: str = Field(default="medium", description="low, medium, high")
    user_stories: List[str] = Field(default_factory=list)
    api_integrations: List[APIIntegration] = Field(default_factory=list)
    acceptance_criteria: List[str] = Field(default_factory=list)
    dependencies: Optional[List[str]] = Field(default_factory=list)

class DesignSystem(BaseModel):
    color_scheme: Optional[str] = Field(default="light", description="Specify any color scheme name or type.")
    primary_colors: Dict[str, str]
    secondary_colors: Dict[str, str]
    ui_component_styles: UIComponentStyle
    design_principles: List[str] = Field(default_factory=list)

class TestingRequirements(BaseModel):
    unit_test_coverage: float = Field(default=80.0, description="Minimum unit test coverage percentage")
    integration_test_scenarios: List[str] = Field(default_factory=list)
    performance_test_scenarios: List[str] = Field(default_factory=list)
    security_test_scenarios: List[str] = Field(default_factory=list)
    test_environments: List[str] = Field(default_factory=lambda: ["development", "staging"])

class ProjectRequirements(BaseModel):
    project_name: str
    description: str
    
    # Core Requirements
    features: List[FeatureRequirement] = Field(default_factory=list)
    pages: List[PageRequirements] = Field(default_factory=list)
    
    # Design System
    design: DesignSystem
    navigation: NavigationMenu

    model_config = ConfigDict(
        validate_assignment = True,
        extra = 'ignore'
    )

ProjectRequirements.model_rebuild()