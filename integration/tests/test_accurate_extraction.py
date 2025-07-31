#!/usr/bin/env python3
"""
Test script using accurate chart parser with corrected cropping.
This version addresses the harsh cropping that was creating inaccurate data.
"""

import os
import sys
import json
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from accurate_chart_parser import AccurateChartParser


def test_accurate_extraction():
    """Test extraction using corrected cropping settings."""
    
    # Initialize accurate parser
    parser = AccurateChartParser(
        scraped_dir="views/charts/scraped/itjobswatch",
        converted_dir="generated"
    )
    
    print("="*60)
    print("TESTING: Accurate Chart Extraction (Corrected Cropping)")
    print("="*60)
    
    # Extract data from artificial intelligence chart
    technology = "artificial-intelligence"
    data_points = parser.extract_technology_data(technology)
    
    if not data_points:
        print("[FAIL] No data points extracted")
        return False
    
    print(f"\n[SUCCESS] Extracted {len(data_points)} data points")
    
    # Convert to dictionary for easier lookup
    data_dict = {year: percentage for year, percentage in data_points}
    
    # Define validation criteria
    validation_points = [
        {"year": 2017, "expected": 0.9, "tolerance": 0.5, "description": "2017 is 0.9% with margin for error"},
        {"year": 2019, "expected": 3.4, "tolerance": 0.5, "description": "2019 is 3.4%"},
        {"year": 2023, "expected": 8.0, "tolerance": 0.5, "description": "2023 is ~8%"}
    ]
    
    print("\n" + "="*60)
    print("VALIDATION RESULTS (Corrected Cropping)")
    print("="*60)
    
    all_tests_passed = True
    results = []
    
    for validation in validation_points:
        year = validation["year"]
        expected = validation["expected"]
        tolerance = validation["tolerance"]
        description = validation["description"]
        
        if year in data_dict:
            actual = data_dict[year]
            min_val = expected - tolerance
            max_val = expected + tolerance
            passed = min_val <= actual <= max_val
            
            status = "[PASS]" if passed else "[FAIL]"
            print(f"{status} {year}: Expected {expected}% (±{tolerance}%), Got {actual:.2f}%")
            print(f"     {description}")
            print(f"     Difference: {abs(actual - expected):.2f}%")
            
            results.append({
                "year": year,
                "expected": expected,
                "actual": actual,
                "tolerance": tolerance,
                "passed": passed,
                "description": description,
                "difference": abs(actual - expected)
            })
            
            if not passed:
                all_tests_passed = False
        else:
            print(f"[FAIL] {year}: No data point found for this year")
            results.append({
                "year": year,
                "expected": expected,
                "actual": None,
                "tolerance": tolerance,
                "passed": False,
                "description": description,
                "error": "No data point found"
            })
            all_tests_passed = False
    
    # Save results
    debug_dir = Path("generated/debug")
    debug_dir.mkdir(parents=True, exist_ok=True)
    
    accurate_data_file = debug_dir / "artificial_intelligence_accurate.json"
    with open(accurate_data_file, 'w') as f:
        json.dump({
            "method": "accurate_extraction_corrected_cropping",
            "technology": technology,
            "total_points": len(data_points),
            "cropping_improvements": {
                "top_percent": 9.0,
                "bottom_percent": 88.0,
                "left_percent": 8.0,
                "right_percent": 95.0,
                "note": "Reduced aggressive cropping to preserve chart data"
            },
            "data_points": [{"year": year, "percentage": pct} for year, pct in data_points],
            "validation_results": results
        }, f, indent=2)
    
    # Analysis
    print("\n" + "="*60)
    print("ACCURATE EXTRACTION ANALYSIS")
    print("="*60)
    
    print("Extracted values with corrected cropping:")
    for validation in validation_points:
        year = validation["year"]
        expected = validation["expected"]
        if year in data_dict:
            actual = data_dict[year]
            improvement_note = ""
            if abs(actual - expected) < 0.5:
                improvement_note = " [Within tolerance]"
            elif abs(actual - expected) < 1.0:
                improvement_note = " [Close]"
            else:
                improvement_note = " [Needs adjustment]"
            print(f"  {year}: {actual:.2f}% (expected: {expected}%){improvement_note}")
    
    print(f"\nDebug images (corrected cropping): generated/debug/")
    print(f"  - artificial_intelligence_corrected_chart_area.png")
    print(f"  - artificial_intelligence_corrected_orange_mask.png")
    print(f"Results saved to: {accurate_data_file}")
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    if all_tests_passed:
        print("[SUCCESS] ALL TESTS PASSED! Corrected cropping achieved target accuracy.")
    else:
        passed_count = sum(1 for r in results if r["passed"])
        total_count = len(results)
        print(f"[PARTIAL] {passed_count}/{total_count} tests passed with corrected cropping.")
        
        avg_difference = sum(r.get("difference", 0) for r in results if "difference" in r) / len([r for r in results if "difference" in r])
        print(f"Average difference from expected: {avg_difference:.2f}%")
        
        if avg_difference < 1.0:
            print("Corrected cropping shows significant improvement!")
        elif avg_difference < 2.0:
            print("Corrected cropping shows moderate improvement.")
        else:
            print("Additional coordinate mapping adjustments may be needed.")
    
    return all_tests_passed


if __name__ == "__main__":
    success = test_accurate_extraction()
    exit_code = 0 if success else 1
    print(f"\nExiting with code: {exit_code}")
    sys.exit(exit_code)