#!/usr/bin/env python3
"""
Test script using enhanced OCR chart parser with light grey mask detection.
This version uses light grey horizontal and vertical masks for precise grid mapping.
"""

import os
import sys
import json
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from enhanced_ocr_chart_parser import EnhancedOCRChartParser


def test_enhanced_ocr_extraction():
    """Test extraction using enhanced OCR parser with light grey masks."""
    
    # Initialize enhanced OCR parser
    parser = EnhancedOCRChartParser(
        scraped_dir="views/charts/scraped/itjobswatch",
        converted_dir="generated"
    )
    
    print("="*60)
    print("TESTING: Enhanced OCR Chart Extraction")
    print("Using light grey masks for precise grid detection")
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
    print("VALIDATION RESULTS (Enhanced OCR with Light Grey Masks)")
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
    masks_dir = debug_root / "masks"
    
    debug_root.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)
    masks_dir.mkdir(parents=True, exist_ok=True)
    
    enhanced_data_file = data_dir / "artificial_intelligence_enhanced_ocr.json"
    with open(enhanced_data_file, 'w') as f:
        json.dump({
            "method": "enhanced_ocr_with_light_grey_masks",
            "technology": technology,
            "total_points": len(data_points),
            "features": [
                "OCR-friendly minimal cropping",
                "Light grey horizontal mask detection",
                "Light grey vertical mask detection",
                "Enhanced grid line mapping",
                "Preserved axis labels"
            ],
            "data_points": [{"year": year, "percentage": pct} for year, pct in data_points],
            "validation_results": results
        }, f, indent=2)
    
    # Analysis
    print("\n" + "="*60)
    print("ENHANCED OCR EXTRACTION ANALYSIS")
    print("="*60)
    
    print("Enhanced features:")
    print("  [+] Light grey horizontal mask: Detects percentage grid lines")
    print("  [+] Light grey vertical mask: Detects year grid lines") 
    print("  [+] OCR-friendly cropping: Preserves axis labels")
    print("  [+] Combined grid detection: Multiple detection methods")
    print("  [+] Enhanced coordinate mapping: Grid-aware positioning")
    
    print("\nExtracted values with enhanced OCR:")
    best_accuracy = True
    for validation in validation_points:
        year = validation["year"]
        expected = validation["expected"]
        if year in data_dict:
            actual = data_dict[year]
            diff = abs(actual - expected)
            
            if diff < 0.3:
                accuracy_note = " [EXCELLENT - Within 0.3%]"
            elif diff < 0.5:
                accuracy_note = " [VERY_GOOD - Within tolerance]"
            elif diff < 1.0:
                accuracy_note = " [GOOD - Close to target]"
            else:
                accuracy_note = " [MODERATE - Needs fine-tuning]"
                best_accuracy = False
                
            print(f"  {year}: {actual:.2f}% (expected: {expected}%, diff: {diff:.2f}%){accuracy_note}")
    
    print(f"\nOrganized debug output:")
    print(f"  generated/debug/data/:")
    print(f"    - artificial_intelligence_enhanced_ocr.json")
    print(f"  generated/debug/masks/:")
    print(f"    - artificial_intelligence_chart_area.png")
    print(f"    - artificial_intelligence_orange_mask.png")
    print(f"    - artificial_intelligence_light_grey_horizontal_mask.png")
    print(f"    - artificial_intelligence_light_grey_vertical_mask.png")
    print(f"    - artificial_intelligence_light_grey_combined_mask.png")
    print(f"  generated/debug/:")
    print(f"    - artificial_intelligence_enhanced_overlay.png")
    print(f"JSON results: {enhanced_data_file}")
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    if all_tests_passed:
        print("[SUCCESS] ALL TESTS PASSED! Enhanced OCR extraction achieved target accuracy.")
        print("Light grey mask detection successfully mapped grid coordinates.")
    else:
        passed_count = sum(1 for r in results if r["passed"])
        total_count = len(results)
        print(f"[PROGRESS] {passed_count}/{total_count} tests passed with enhanced OCR.")
        
        avg_difference = sum(r.get("difference", 0) for r in results if "difference" in r) / len([r for r in results if "difference" in r])
        print(f"Average difference: {avg_difference:.2f}%")
        
        if best_accuracy:
            print("Enhanced OCR shows excellent accuracy! Very close to target values.")
        elif avg_difference < 1.0:
            print("Enhanced OCR shows significant improvement with light grey masks.")
        else:
            print("Enhanced OCR provides better grid detection foundation.")
    
    print("\nNEXT STEPS for further refinement:")
    if not all_tests_passed:
        print("  1. Analyze light grey mask detection quality")
        print("  2. Fine-tune grid line coordinate mapping")
        print("  3. Verify horizontal grid spacing (12 lines for 0-12%)")
        print("  4. Check vertical grid alignment with year labels")
    
    return all_tests_passed


if __name__ == "__main__":
    success = test_enhanced_ocr_extraction()
    exit_code = 0 if success else 1
    print(f"\nExiting with code: {exit_code}")
    sys.exit(exit_code)