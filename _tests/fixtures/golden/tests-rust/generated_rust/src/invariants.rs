// Generated Rust invariant stubs from a validated DeepThought catalog.
use crate::types::GeneratedInvariant;

#[test]
#[ignore = "Generated invariant stub: connect this to a concrete model validator"]
fn thing_thing_name_present() {
    let invariant = GeneratedInvariant {
        model: r#"thing"#.to_string(),
        source: r#"source: `model/thing.yaml`"#.to_string(),
        assertion: Some(r#{"field":"thing_name"}#.to_string()),
        enforcement: Some(r#"always"#.to_string()),
        raises: None,
    };
    let _ = invariant;
    unreachable!("Generated invariant stub");
}
