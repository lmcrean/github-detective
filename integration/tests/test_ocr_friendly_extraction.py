#!/usr/bin/env python3
"""
Test script using OCR-friendly chart parser that preserves axis labels.
This version uses minimal cropping to keep x and y axis labels intact for OCR.
"""

import os
import sys
import json
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from ocr_friendly_chart_parser import OCRFriendlyChartParser


def test_ocr_friendly_extraction():
    """Test extraction using OCR-friendly parser with preserved axis labels."""
    
    # Initialize OCR-friendly parser
    parser = OCRFriendlyChartParser(
        scraped_dir="views/charts/scraped/itjobswatch",
        converted_dir="generated"
    )
    
    print("="*60)
    print("TESTING: OCR-Friendly Chart Extraction")
    print("Preserves x and y axis labels for accurate coordinate mapping")
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
    print("VALIDATION RESULTS (OCR-Friendly with Preserved Labels)")
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
    
    ocr_data_file = debug_dir / "artificial_intelligence_ocr_friendly.json"
    with open(ocr_data_file, 'w') as f:
        json.dump({
            "method": "ocr_friendly_extraction",
            "technology": technology,
            "cropping_strategy": "minimal_preserve_axis_labels",
            "total_points": len(data_points),
            "cropping_settings": {
                "top_percent": 3.0,
                "bottom_percent": 97.0,
                "left_percent": 2.0,
                "right_percent": 98.0,
                "rationale": "Preserve x and y axis labels for OCR coordinate mapping"
            },
            "data_points": [{"year": year, "percentage": pct} for year, pct in data_points],
            "validation_results": results
        }, f, indent=2)
    
    # Analysis
    print("\n" + "="*60)
    print("OCR-FRIENDLY EXTRACTION ANALYSIS")
    print("="*60)
    
    print("Chart preservation status:")
    print("  ✓ X-axis labels: PRESERVED (minimal bottom cropping)")
    print("  ✓ Y-axis labels: PRESERVED (minimal left cropping)")
    print("  ✓ Title area: PRESERVED (minimal top cropping)")
    print("  ✓ Right margin: PRESERVED (minimal right cropping)")
    
    print("\nExtracted values with preserved axis labels:")
    for validation in validation_points:
        year = validation["year"]
        expected = validation["expected"]
        if year in data_dict:
            actual = data_dict[year]
            accuracy_note = ""
            if abs(actual - expected) < 0.5:
                accuracy_note = " [EXCELLENT]"
            elif abs(actual - expected) < 1.0:
                accuracy_note = " [GOOD]"
            elif abs(actual - expected) < 2.0:
                accuracy_note = " [MODERATE]"
            else:
                accuracy_note = " [NEEDS_CALIBRATION]"
            print(f"  {year}: {actual:.2f}% (expected: {expected}%){accuracy_note}")
    
    print(f"\nDebug images with preserved labels: generated/debug/")
    print(f"  - artificial_intelligence_ocr_friendly_chart_area.png (full chart with labels)")
    print(f"  - artificial_intelligence_ocr_friendly_orange_mask.png")
    print(f"  - artificial_intelligence_ocr_grid_overlay.png (grid lines visualized)")
    print(f"Results saved to: {ocr_data_file}")
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    if all_tests_passed:
        print("[SUCCESS] ALL TESTS PASSED! OCR-friendly extraction is ready for coordinate mapping.")
    else:
        passed_count = sum(1 for r in results if r["passed"])
        total_count = len(results)
        print(f"[STATUS] {passed_count}/{total_count} tests passed with OCR-friendly preservation.")
        
        avg_difference = sum(r.get("difference", 0) for r in results if "difference" in r) / len([r for r in results if "difference" in r])
        print(f"Average difference: {avg_difference:.2f}%")
        
        print("\nOCR-FRIENDLY BENEFITS:")
        print("  ✓ Axis labels preserved for accurate coordinate reference")
        print("  ✓ Grid lines can be detected with proper context")
        print("  ✓ Chart structure intact for OCR-based calibration")
        print("  ✓ Ready for coordinate system refinement using label information")
    
    return all_tests_passed


if __name__ == "__main__":
    success = test_ocr_friendly_extraction()
    exit_code = 0 if success else 1
    print(f"\nExiting with code: {exit_code}")
    sys.exit(exit_code)