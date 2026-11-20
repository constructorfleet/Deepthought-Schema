// Shared helper types for generated DeepThought Rust stubs.
#[derive(Debug, Clone)]
pub struct GeneratedScenario {
    pub source: String,
    pub given: Vec<String>,
    pub when: Option<String>,
    pub then: Vec<String>,
}

#[derive(Debug, Clone)]
pub struct GeneratedInvariant {
    pub model: String,
    pub source: String,
    pub assertion: Option<String>,
    pub enforcement: Option<String>,
    pub raises: Option<String>,
}
