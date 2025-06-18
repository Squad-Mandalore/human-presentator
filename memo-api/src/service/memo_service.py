# import torch
# from memo import inference
# from importlib import resources
# import gc
# import os


# def generate_from_picture_and_audio(
#     filepath_picture: str, filepath_audio: str, output_path: str
# ):
#     try:
#         # Set environment variables for memory optimization
#         os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:64,expandable_segments:True'

#         # Clear GPU cache before processing
#         if torch.cuda.is_available():
#             torch.cuda.empty_cache()
#             torch.cuda.synchronize()
#             gc.collect()

#             # Print memory usage for debugging
#             allocated = torch.cuda.memory_allocated() / 1024**3
#             reserved = torch.cuda.memory_reserved() / 1024**3
#             print(f"GPU Memory before memo - Allocated: {allocated:.2f}GB, Reserved: {reserved:.2f}GB")

#         # Use the memory-optimized config that enables CPU offloading
#         config_path = get_resource_path("configs", "inference_memory_optimized.yaml")

#         args = [
#             "--config", config_path,
#             "--input_image", filepath_audio,  # Note: these are swapped in original code
#             "--input_audio", filepath_picture,
#             "--output_dir", output_path,
#         ]

#         print("Starting memo inference with CPU offloading enabled...")
#         inference.main(args)
#         print("Memo inference completed successfully!")

#         # Clear GPU cache after processing
#         if torch.cuda.is_available():
#             torch.cuda.empty_cache()
#             torch.cuda.synchronize()
#             gc.collect()

#     except Exception as err:
#         print(f"Error in memo generation: {err}")
#         # Clear cache even on error
#         if torch.cuda.is_available():
#             torch.cuda.empty_cache()
#             torch.cuda.synchronize()
#             gc.collect()
#         raise err


# def get_resource_path(dir: str, file: str) -> str:
#     with resources.path(f"memo.{dir}", file) as p:
#         return str(p)

import torch
from memo import inference
from importlib import resources
import gc


def clear_gpu_memory():
    """Clear GPU memory cache"""
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        torch.cuda.synchronize()
        gc.collect()


def generate_from_picture_and_audio(
    filepath_picture: str, filepath_audio: str, output_path: str
):
    try:
        # Clear GPU memory before processing
        clear_gpu_memory()
        
        args = [
            "--config",
            get_resource_path("configs", "inference.yaml"),
            "--input_image",
            filepath_audio,
            "--input_audio",
            filepath_picture,
            "--output_dir",
            output_path,
            # "--seed", "1234",
        ]

        inference.main(args)
        
    except Exception as err:
        print(err)
        raise err
    finally:
        # Always clear GPU memory after processing (success or failure)
        clear_gpu_memory()


def get_resource_path(dir: str, file: str) -> str:
    with resources.path(f"memo.{dir}", file) as p:
        return str(p)
