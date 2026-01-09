# 我的博客

这是一个使用 GitHub Pages 托管的静态博客网站。

## 项目结构

```
blog/
├── index.html          # 博客首页
├── about.html          # 关于页面
├── archive.html        # 文章归档页面
├── css/
│   └── style.css      # 样式文件
├── posts/             # 博客文章目录
│   ├── getting-started-with-github-pages.html
│   ├── css-flexbox-guide.html
│   ├── new-year-resolutions.html
│   └── static-site-generators.html
└── README.md          # 本文件
```

## 如何部署到 GitHub Pages

### 方法一：使用 GitHub 网页界面

1. **创建仓库**
   - 登录 GitHub
   - 点击右上角的 "+" 号，选择 "New repository"
   - 仓库名可以是：
     - `username.github.io`（个人主页，网站地址为 `https://username.github.io`）
     - 任意名称（项目站点，网站地址为 `https://username.github.io/repository-name`）

2. **上传文件**
   - 在仓库页面点击 "uploading an existing file"
   - 将 `blog` 文件夹中的所有文件上传到仓库根目录
   - 或者，如果仓库名是 `username.github.io`，直接上传所有文件
   - 如果仓库名是其他名称，可以将文件上传到根目录或 `docs` 文件夹

3. **启用 GitHub Pages**
   - 进入仓库的 "Settings"（设置）
   - 在左侧菜单找到 "Pages"
   - 在 "Source" 部分：
     - 选择分支（通常是 `main` 或 `master`）
     - 选择文件夹（`/` 根目录 或 `/docs`）
   - 点击 "Save"（保存）

4. **访问网站**
   - 等待几分钟让 GitHub 构建网站
   - 访问 `https://username.github.io` 或 `https://username.github.io/repository-name`

### 方法二：使用 Git 命令行

1. **初始化 Git 仓库**
   ```bash
   cd blog
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **连接到 GitHub 仓库**
   ```bash
   git remote add origin https://github.com/username/repository-name.git
   git branch -M main
   git push -u origin main
   ```

3. **启用 GitHub Pages**
   - 按照方法一的步骤 3 在 GitHub 网页上启用 Pages

## 重要提示

### 路径问题

✅ **正确**：使用相对路径
```html
<link rel="stylesheet" href="css/style.css">
<a href="posts/article.html">文章</a>
<a href="../index.html">返回首页</a>
```

❌ **错误**：使用绝对路径
```html
<link rel="stylesheet" href="/css/style.css">
<a href="/posts/article.html">文章</a>
```

### 文件组织

- 如果仓库名是 `username.github.io`，所有文件放在根目录
- 如果仓库名是其他名称，文件可以放在根目录或 `docs` 文件夹
- 确保 `index.html` 在正确的目录中

### 更新网站

每次您推送新的更改到 GitHub 仓库后，GitHub Pages 会自动重新构建网站。通常需要几分钟时间。

## 自定义域名（可选）

如果您有自己的域名：

1. 在仓库根目录创建 `CNAME` 文件
2. 文件内容为您的域名，例如：`blog.example.com`
3. 在您的域名 DNS 设置中添加 CNAME 记录：
   - 名称：`blog`（或 `@` 表示根域名）
   - 值：`username.github.io`
4. 在 GitHub Pages 设置中也可以配置自定义域名

## 添加新文章

1. 在 `posts/` 文件夹中创建新的 HTML 文件
2. 使用相同的 HTML 结构和样式
3. 在 `index.html` 和 `archive.html` 中添加文章链接
4. 提交并推送到 GitHub

## 技术说明

- 所有文件使用相对路径，确保在 GitHub Pages 上正常工作
- 响应式设计，适配各种设备
- 纯静态 HTML/CSS/JavaScript，无需服务器端处理
- 兼容所有现代浏览器

## 许可证

本项目采用 MIT 许可证。

## 参考资源

- [GitHub Pages 官方文档](https://docs.github.com/en/pages)
- [GitHub Pages 入门指南](https://pages.github.com/)

