// Shared helper types for generated DeepThought TypeScript stubs.

export type JsonValue =
  | null
  | boolean
  | number
  | string
  | JsonValue[]
  | { [key: string]: JsonValue };

export interface GeneratedScenario {
  source: string;
  given: JsonValue[];
  when: JsonValue | null;
  then: JsonValue[];
}

export interface GeneratedInvariant {
  model: string;
  source: string;
  assertion: JsonValue | null;
  enforcement: JsonValue | null;
  raises: string | null;
}
