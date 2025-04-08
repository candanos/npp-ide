import chardet
from typing import Tuple, Optional
import codecs

class EncodingFixer:
    def __init__(self):
        self.common_encodings = [
            'utf-8', 'iso-8859-1', 'iso-8859-2', 'windows-1250', 
            'windows-1252', 'ascii', 'latin1', 'cp1250', 'cp1252'
        ]

    def detect_encoding(self, binary_data: bytes) -> Tuple[str, float]:
        """
        Detect the encoding of binary data using chardet.
        
        Args:
            binary_data (bytes): The binary data to analyze
            
        Returns:
            Tuple[str, float]: Detected encoding and confidence score
        """
        result = chardet.detect(binary_data)
        return result['encoding'], result['confidence']

    def try_decode(self, binary_data: bytes, encoding: str) -> Optional[str]:
        """
        Attempt to decode binary data with a specific encoding.
        
        Args:
            binary_data (bytes): The binary data to decode
            encoding (str): The encoding to try
            
        Returns:
            Optional[str]: Decoded string if successful, None if failed
        """
        try:
            return binary_data.decode(encoding)
        except UnicodeDecodeError:
            return None

    def fix_encoding(self, binary_data: bytes) -> Tuple[str, str, float]:
        """
        Attempt to fix encoding issues by trying multiple encodings.
        
        Args:
            binary_data (bytes): The binary data to fix
            
        Returns:
            Tuple[str, str, float]: Fixed text, used encoding, and confidence score
        """
        # First try chardet detection
        detected_encoding, confidence = self.detect_encoding(binary_data)
        
        if detected_encoding:
            result = self.try_decode(binary_data, detected_encoding)
            if result:
                return result, detected_encoding, confidence

        # Try common encodings if chardet detection failed
        for encoding in self.common_encodings:
            result = self.try_decode(binary_data, encoding)
            if result:
                return result, encoding, 1.0

        raise ValueError("Could not decode the binary data with any known encoding")

    def fix_file(self, input_path: str, output_path: str) -> Tuple[str, float]:
        """
        Fix encoding issues in a file and save the result.
        
        Args:
            input_path (str): Path to the input file
            output_path (str): Path to save the fixed file
            
        Returns:
            Tuple[str, float]: Used encoding and confidence score
        """
        with open(input_path, 'rb') as f:
            binary_data = f.read()

        fixed_text, encoding, confidence = self.fix_encoding(binary_data)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(fixed_text)
            
        return encoding, confidence

def main():
    # Example usage
    fixer = EncodingFixer()
    
    # Example with binary data
    sample_bytes = b'This is some text with \x80 invalid UTF-8 bytes'
    sample_bytes = b'PÓªªO¥YSKO'
    try:
        fixed_text, encoding, confidence = fixer.fix_encoding(sample_bytes)
        print(f"Fixed text: {fixed_text}")
        print(f"Used encoding: {encoding} (confidence: {confidence:.2f})")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Example with file
    try:
        encoding, confidence = fixer.fix_file('input.txt', 'output.txt')
        print(f"File fixed using {encoding} encoding (confidence: {confidence:.2f})")
    except (ValueError, IOError) as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    main()