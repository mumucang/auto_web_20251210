
import logging
import datetime
import os

from config import logs_path


class LoggerUtil:
    _logger = None

    @classmethod
    def get_logger(cls, name='default_logger', level=logging.INFO, file_name=None):
        if cls._logger is None:
            # 创建日志器对象
            cls._logger = logging.getLogger(name)
            cls._logger.setLevel(level)

            # 创建处理器
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)

            if file_name:
                # 使用本地时间生成日志文件名
                timestamp = datetime.datetime.now().strftime('%Y%m%d')
                file_name_with_timestamp = os.path.join(logs_path, f'{file_name}_{timestamp}.log')
                file_handler = logging.FileHandler(file_name_with_timestamp,encoding='utf-8')
                file_handler.setLevel(level)

            # 创建格式化器
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            # 将格式化器添加到处理器
            console_handler.setFormatter(formatter)
            if file_name:
                file_handler.setFormatter(formatter)

            # 将处理器添加到日志器
            cls._logger.addHandler(console_handler)
            if file_name:
                cls._logger.addHandler(file_handler)

        return cls._logger

if __name__ == '__main__':
    # 使用示例
    logger = LoggerUtil.get_logger(name='my_web_logger', level=logging.DEBUG, file_name='web')
    logger.info('这是一个信息级别的日志')
    logger.debug('这是一个调试级别的日志')

