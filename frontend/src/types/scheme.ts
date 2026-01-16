// src/types/scheme.ts
export interface EligibilityCheck {
  condition: string;
  satisfied: boolean;
}

export interface SchemeResponse {
  name: string;
  eligibility_checks: EligibilityCheck[];
  benefits: string;
}
