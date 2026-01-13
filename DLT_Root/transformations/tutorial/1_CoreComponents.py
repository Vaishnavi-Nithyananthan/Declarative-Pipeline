# import dlt

# # Create Streaming Table

# @dlt.table (
#     name = "first_stream_table"
# )
# def first_stream_table():
#     df = spark.readStream.table("dlt_vaish.source.orders")
#     return df


# # Create Materialized View

# @dlt.table(
#     name = "first_mat_view"
# )
# def first_mat_view():
#     df = dlt.read("dlt_vaish.source.orders")
#     return df


# # Create Views

# @dlt.view(
#     name = "first_batch_view"
# )
# def first_batch_view():
#     df = spark.read.table("dlt_vaish.source.orders")
#     return df


# #Create Streaming View
# @dlt.view(
#     name = "first_stream_view"
# ) 
# def first_stream_view():
#     df = spark.readStream.table("dlt_vaish.source.orders")
#     return df
