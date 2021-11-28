#! /usr/bin/env python3

import sys

from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}")


def list_blobs(bucket_name):
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        print(blob.name)


def list_blobs_with_prefix(bucket_name, prefix, delimiter=None):
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name, prefix=prefix, delimiter=delimiter)

    print("Blobs")
    for blob in blobs:
        print(blob.name)

    if delimiter:
        print("Prefixes")
        for prefix in blobs.prefixes:
            print(prefix)


def do_help(bucket_name, *args, **kwargs):
    pass


def do_ls(bucket_name, *args, **kwargs):
    print(bucket_name)
    print(*args)
    list_blobs(bucket_name)
    # list_blobs_with_prefix(bucket_name, *args)


def do_upload(bucket_name, *args, **kwargs):
    source_name, dest_name = args

    # upload_blob(bucket_name, source_name, dest_name)
    pass


def do_download(bucket_name, *args, **kwargs):
    pass


def do_rename(bucket_name, *args, **kwargs):
    pass


def do_delete(bucket_name, *args, **kwargs):
    pass


if __name__ == "__main__":
    print(sys.argv)

    cmd = 'help'
    bucket_name = None
    if len(sys.argv)  > 1:
        cmd = sys.argv[1]
    if len(sys.argv) > 2:
        bucket_name = sys.argv[2]
    params = tuple(sys.argv[3:])

    print(f'{cmd=}\n{bucket_name=}\n{params=}\n')

    do_fn = locals()[f'do_{cmd}']
    do_fn(bucket_name, params)

