def parse_code(code):
    allocations = []  
    errors = []
    
# BufferOverflow

    for line in code.splitlines():
        
        if 'malloc' in line or 'calloc' in line:
            size = extract_malloc_size(line)
            allocations.append(size)


        if 'ptr[' in line or 'ptr++' in line:
            ptr_access = extract_pointer_access(line)
            for alloc_size in allocations:
                if ptr_access > alloc_size:
                    errors.append(f"Pointer access exceeds allocated size: {line}")

   
        if 'for' in line:
            loop_condition = extract_loop_condition(line)
            array_size = extract_array_size(line)
            if loop_condition >= array_size:
                errors.append(f"Off-by-one error in loop condition: {line}")

    return errors

def extract_malloc_size(line):
    pass

def extract_pointer_access(line):
    pass

def extract_loop_condition(line):
    pass

def extract_array_size(line):
    pass
