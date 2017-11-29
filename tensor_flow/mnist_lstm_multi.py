import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.python.ops import rnn, rnn_cell

# configuration
#                        O * W + b -> 10 labels for each image, O[? 28], W[28 10], B[10]
#                       ^ (O: output 28 vec from 28 vec input)
#                       |
#      +-+  +-+       +--+
#      |1|->|2|-> ... |28| time_step_size = 28
#      +-+  +-+       +--+
#       ^    ^    ...  ^
#       |    |         |
# img1:[28] [28]  ... [28]
# img2:[28] [28]  ... [28]
# img3:[28] [28]  ... [28]
# ...
# img128 or img256 (batch_size or test_size 256)
#      each input size = input_vec_size=lstm_size=28

# configuration variables
mnist = input_data.read_data_sets("/home/tom/mnist_data/", one_hot = True)

hm_epochs = 2
n_classes = 10
batch_size = 128
input_vec_size = 28  # 输入向量的维度
time_step_size = 28  # 循环层长度
rnn_size = 141 #the layer will contain multiple parallel LSTM units,
layer_num=2

#the

# structurally identical but each eventually
# "learning to remember" some different thing.

#o make the name num_units more intuitive, you can think of
# it as the number of hidden units in the LSTM cell,
# or the number of memory units in the cell.

#the hidden units represent tangible storage within the network, which is manifest primarily
# in the size of the weights array. And because an LSTM actually does have a bit of it's
# own internal storage separate from the learned model parameters, it has to know
# how many units there are -- which ultimately needs to agree with the size of the weights.
#  In the simplest case, an RNN has no internal storage --
# so it doesn't even need to know in advance how many "hidden units" it is being applied to.

#基础参数： data_dim， timesteps， num_classes   分别为 28，28， 10
# 网络层级 ：    LSTM ----》LSTM ----》LSTM ----》Dense
# 注意点： input_shape=(timesteps, data_dim+14))   此处 应该为  data_dim ， data_dim+14是我做第二个试验使用。
# 网络理解： RNN是用前一部分数据对当前数据的影响，并共同作用于最后结果。 用基础的深度神经网络（只有Dense层），是把MNIST一个图形，
# 提取成784个像素数据，把784个数据扔给神经网络，784个数据是同等的概念。 训练出权重来确定最终的分类值。
#
# RNN 之于MNIST， 是把MNIST 分成 28x28 数据。可以理解为用一个激光扫描一个图片，扫成28个（行）数据， 每行为28个像素。 站在时间序列
# 的角度，其实图片没有序列概念。但是我们可以这样理解， 每一行于下一行是有位置关系的，不能进行顺序变化。 比如一个手写 “7”字， 如果把28行
# 的上下行顺序打乱， 那么7 上面的一横就可能在中间位置，也可能在下面的位置。  这样，最终的结果就不应该是 7 .
# 所以MNIST 的 28x28可以理解为 有时序关系的数据。

x = tf.placeholder('float', [None, time_step_size,input_vec_size])
y = tf.placeholder('float')
pro=tf.Variable(0.5)

def recurrent_neural_network(x,keep_prob):
    layer = {'weights':tf.Variable(tf.random_normal([rnn_size,n_classes])),
             'biases':tf.Variable(tf.random_normal([n_classes]))}
    X = tf.reshape(x, [-1, 28, 28])

    # **步骤2：定义一层 LSTM_cell，只需要说明 hidden_size, 它会自动匹配输入的 X 的维度
    lstm_cell = rnn_cell.BasicLSTMCell(num_units=123, forget_bias=1.0, state_is_tuple=True)

    # **步骤3：添加 dropout layer, 一般只设置 output_keep_prob
    lstm_cell = rnn_cell.DropoutWrapper(cell=lstm_cell, input_keep_prob=1.0, output_keep_prob=keep_prob)

    # **步骤4：调用 MultiRNNCell 来实现多层 LSTM
    mlstm_cell = rnn_cell.MultiRNNCell([lstm_cell] * layer_num, state_is_tuple=True)

    # **步骤5：用全零来初始化state

    outputs, state = tf.nn.dynamic_rnn(mlstm_cell,  dtype=tf.float32,inputs=X, time_major=False)
    # X, input shape: (batch_size, time_step_size, input_vec_size)
    # XT shape: (time_step_size, batch_size, input_vec_size)
    # xt = tf.transpose(x, [1,0,2],name = 'xt')  # permute time_step_size and batch_size,[28, 128, 28]

    # XR shape: (time_step_size * batch_size, input_vec_size)
    # xr = tf.reshape(xt, [-1, input_vec_size],name = 'xr') # each row has input for each lstm cell (lstm_size=input_vec_size)
    #
    # # Each array shape: (batch_size, input_vec_size)
    # X_split = tf.split(xr, time_step_size, 0,name = 'X_split') # split them to time_step_size (28 arrays),shape = [(128, 28),(128, 28)...]



    lstm_cell = rnn_cell.BasicLSTMCell(rnn_size,state_is_tuple=True)

    # # **步骤3：添加 dropout layer, 一般只设置 output_keep_prob
    # lstm_cell = rnn_cell.DropoutWrapper(cell=lstm_cell, input_keep_prob=1.0, output_keep_prob=keep_prob)
    #
    # # **步骤4：调用 MultiRNNCell 来实现多层 LSTM
    mlstm_cell = rnn_cell.MultiRNNCell([lstm_cell] * layer_num, state_is_tuple=True)
    #
    # # **步骤5：用全零来初始化state
    # The solution is to use a variable batch_size based on the size of the X value,
    #  and to then generate a variable initial_state dynamically based on this:
    batch_size_t = tf.shape(x)[0]
    init_state = mlstm_cell.zero_state(batch_size_t, dtype=tf.float32)



    # init_state = lstm_cell.zero_state(batch_size_t, dtype=tf.float32)

    # outputs, states = rnn.static_rnn(lstm_cell, X_split, dtype=tf.float32)
    outputs, final_state  = tf.nn.dynamic_rnn(mlstm_cell, x,  time_major=False)

    # outputs, final_state = tf.nn.dynamic_rnn(
    #     cell=rnn_cell,  # 选择传入的cell
    #     inputs=image,  # 传入的数据
    #     initial_state=None,  # 初始状态
    #     dtype=tf.float32,  # 数据类型
    #     time_major=False,  # False: (batch, time step, input); True: (time step, batch, input)，这里根据image结构选择False
    # )

    output = tf.matmul(outputs[:, -1, :],layer['weights']) + layer['biases']
    # merged_summary_op = tf.summary.merge_all()
    return output


def train_neural_network(x):

    prediction = recurrent_neural_network(x, pro)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))

    optimizer = tf.train.AdamOptimizer().minimize(cost)

    tf.summary.scalar('loss_function', cost)

    merged_summary_op = tf.summary.merge_all()

    if tf.gfile.Exists("/tmp/mnist_logs"):
        tf.gfile.DeleteRecursively("/tmp/mnist_logs");

    with tf.Session() as sess:
        summary_writer = tf.summary.FileWriter('/tmp/mnist_logs', sess.graph)
        sess.run(tf.initialize_all_variables())


        for epoch in range(hm_epochs):
            epoch_loss = 0
            for _ in range(int(mnist.train.num_examples / batch_size)):
                epoch_x, epoch_y = mnist.train.next_batch(batch_size)
                epoch_x = epoch_x.reshape((batch_size, time_step_size, input_vec_size))

                ee, c = sess.run([optimizer, cost], feed_dict={x: epoch_x, y: epoch_y,pro:0.5})
                epoch_loss += c

                # summary_writer.add_summary(ee, epoch);

            print('Epoch', epoch, 'completed out of', hm_epochs, 'loss:', epoch_loss)
            # summary_writer.add_summary(epoch_loss, epoch);
        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        # et=sess.run(accuracy, feed_dict={x: mnist.test.images.reshape(-1, time_step_size, input_vec_size),y: mnist.test.labels,pro:1})


        print('Accuracy:',
          accuracy.eval({x: mnist.test.images.reshape((-1, time_step_size, input_vec_size)), y: mnist.test.labels}))
        #
        # print "test accuracy %g"% sess.run(accuracy, feed_dict={
        #     _X: mnist.test.images, y: mnist.test.labels, keep_prob: 1.0, batch_size:mnist.test.images.shape[0]})

train_neural_network(x)