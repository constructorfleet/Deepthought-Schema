// Shared helper types for generated DeepThought Go stubs.
package generatedtests

type GeneratedScenario struct {
	Source string
	Given  []string
	When   *string
	Then   []string
}

type GeneratedInvariant struct {
	Model       string
	Source      string
	Assertion   *string
	Enforcement *string
	Raises      *string
}

func stringPtr(value string) *string {
	return &value
}
