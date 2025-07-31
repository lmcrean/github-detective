#!/usr/bin/env python3
"""
Test script using structure-based chart parser that detects lines by geometry.
This approach should be more reliable than color-based detection.
"""

import os
import sys
import json
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from structure_based_chart_parser import StructureBasedChartParser


def test_structure_based_extraction():
    """Test extraction using structure-based line detection."""
    
    # Initialize structure-based parser
    parser = StructureBasedChartParser(
        scraped_dir="views/charts/scraped/itjobswatch",
        converted_dir="generated"
    )
    
    print("="*60)
    print("TESTING: Structure-Based Chart Extraction")
    print("Detects grid lines by geometric structure, not color")
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
    print("VALIDATION RESULTS (Structure-Based Detection)")
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
    
    # Save results to organized directory structure
    debug_root = Path("generated/debug")
    data_dir = debug_root / "data"
    
    debug_root.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)
    
    structure_data_file = data_dir / "artificial_intelligence_structure_based.json"
    with open(structure_data_file, 'w') as f:
        json.dump({
            "method": "structure_based_line_detection",
            "technology": technology,
            "total_points": len(data_points),
            "features": [
                "OCR-friendly minimal cropping",
                "Geometric structure-based line detection",
                "Horizontal edge detection (Sobel filter)",
                "Vertical edge detection (Sobel filter)",
                "Grid line filtering and spacing analysis"
            ],
            "data_points": [{"year": year, "percentage": pct} for year, pct in data_points],
            "validation_results": results
        }, f, indent=2)
    
    # Analysis
    print("\n" + "="*60)
    print("STRUCTURE-BASED EXTRACTION ANALYSIS")
    print("="*60)
    
    print("Structure-based features:")
    print("  [+] Geometric line detection: Finds lines by structure, not color")
    print("  [+] Sobel edge detection: Identifies horizontal/vertical patterns")
    print("  [+] Grid filtering: Focuses on evenly-spaced chart grid")
    print("  [+] OCR-friendly: Preserves axis labels for coordinate reference")
    print("  [+] Robust detection: Independent of color variations")
    
    print("\nExtracted values with structure-based detection:")
    accuracy_summary = {"excellent": 0, "good": 0, "moderate": 0, "poor": 0}
    
    for validation in validation_points:
        year = validation["year"]
        expected = validation["expected"]
        if year in data_dict:
            actual = data_dict[year]
            diff = abs(actual - expected)
            
            if diff < 0.3:
                accuracy_note = " [EXCELLENT]"
                accuracy_summary["excellent"] += 1
            elif diff < 0.5:
                accuracy_note = " [VERY_GOOD - Within tolerance]"
                accuracy_summary["good"] += 1
            elif diff < 1.0:
                accuracy_note = " [GOOD - Close to target]"
                accuracy_summary["good"] += 1
            elif diff < 2.0:
                accuracy_note = " [MODERATE]"
                accuracy_summary["moderate"] += 1
            else:
                accuracy_note = " [NEEDS_WORK]"
                accuracy_summary["poor"] += 1
                
            print(f"  {year}: {actual:.2f}% (expected: {expected}%, diff: {diff:.2f}%){accuracy_note}")
    
    print(f"\nOrganized debug output:")
    print(f"  generated/debug/data/:")
    print(f"    - artificial_intelligence_structure_based.json")
    print(f"  generated/debug/masks/:")
    print(f"    - artificial_intelligence_chart_area.png")
    print(f"    - artificial_intelligence_orange_mask.png")
    print(f"    - artificial_intelligence_horizontal_edges.png")
    print(f"    - artificial_intelligence_vertical_edges.png")
    print(f"  generated/debug/:")
    print(f"    - artificial_intelligence_structure_overlay.png")
    print(f"JSON results: {structure_data_file}")
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    if all_tests_passed:
        print("[SUCCESS] ALL TESTS PASSED! Structure-based detection achieved target accuracy.")
        print("Geometric line detection successfully identified chart grid coordinates.")
    else:
        passed_count = sum(1 for r in results if r["passed"])
        total_count = len(results)
        print(f"[PROGRESS] {passed_count}/{total_count} tests passed with structure-based detection.")
        
        avg_difference = sum(r.get("difference", 0) for r in results if "difference" in r) / len([r for r in results if "difference" in r])
        print(f"Average difference: {avg_difference:.2f}%")
        
        print(f"\nAccuracy distribution:")
        print(f"  Excellent (< 0.3%): {accuracy_summary['excellent']}")
        print(f"  Good (< 1.0%): {accuracy_summary['good']}")
        print(f"  Moderate (< 2.0%): {accuracy_summary['moderate']}")
        print(f"  Needs work (>= 2.0%): {accuracy_summary['poor']}")
        
        if accuracy_summary["excellent"] + accuracy_summary["good"] >= 2:
            print("Structure-based detection shows excellent promise!")
        elif avg_difference < 1.5:
            print("Structure-based detection provides good foundation for refinement.")
        else:
            print("Structure-based detection may need parameter tuning.")
    
    print("\nADVANTAGES of structure-based approach:")
    print("  [+] Color-independent (works with any grid color)")
    print("  [+] Robust to lighting variations")
    print("  [+] Detects actual line geometry")
    print("  [+] Less sensitive to color space conversions")
    
    return all_tests_passed


if __name__ == "__main__":
    success = test_structure_based_extraction()
    exit_code = 0 if success else 1
    print(f"\nExiting with code: {exit_code}")
    sys.exit(exit_code)